--- 
layout: post
title: Fun with custom Zend_Views
---
<p>
The other day I had a nice meeting in my basement lair with my co-workers.  We laughed.  We cried.  We had some BBQ'd burgers, and nobody got food poisoning.  As we discussed the implementation of our new fantasy gaming platform, I managed to figure out that one requirement was for an admin to upload a header and footer file for a game.  "The idea here is to be able to set up a new game for someone without programmer intervention". </p>
<p>
After I got over being insulted that a programmer was not required for every tiny tweak to the site (I'm kidding) I tried to figure out how I was going to accomplish this.  I'm not a big fan of storing actual HTML content in a database.  Call me old-fashioned, but I feel my HTML content belongs on the filesystem, and nowhere else.  Besides, it makes it harder to do deployments of code on multiple servers if all the templates aren't there to begin with.
</p>
<p>
The solution was, of course, obvious:  create a custom Zend_View and override stuff until you get it behaving the way you want!  The logic for doing this is actually quite simple:
<ol>
<li>Check to see if the script in question exists in the file system</li>
<li>If not, figure out what template we need to pull from the database.</li>
<li>Read in contents of that script from the database</li>
<li>Write contents to the filesystem</li>
</ol>
</p>
<p>
<b>NOTE</b>:  I am not sure if this is the most elegant solution for solving this particular problem.  I am open to a different solution so long as it meets the same needs.
</p>
<p>
Since I've made a commitment to doing TDD for this project, naturally I started out with a test:
{% codeblock lang:php %}

< ?php
require_once 'PHPUnit/Framework.php';
require_once 'Zend/Application.php';

// Define path to application directory
if (!defined('APPLICATION_PATH')) {
    define('APPLICATION_PATH', realpath(dirname(__FILE__) . '/../../../application'));
}

// Define application environment
if (!defined('APPLICATION_ENV')) {
    define('APPLICATION_ENV', (getenv('APPLICATION_ENV') ? getenv('APPLICATION_ENV') : 'test'));
}

// Ensure library/ is on include_path
set_include_path(implode(PATH_SEPARATOR, array(
        realpath(APPLICATION_PATH . '/../library'),
            get_include_path(),
        )));

class Xmlteam_ZFViewTest extends PHPUnit_Framework_TestCase 
{

    public function setUp()
    {
        $this->bootstrap = new Zend_Application(
            'testing',
            APPLICATION_PATH . '/configs/application.ini'
        );
        parent::setUp();
    }

    public function tearDown()
    {
        parent::tearDown();
    }

    
    public function testRenderView()
    {
        $templateData = array(
            'league_short_name' => 'testing',
            'type' => 'header',
            'created_at' => new Doctrine_Expression('NOW()'),
            'content' => '<div id="header"><b>header</b></div>'
        );
        $testTemplate = new Template();
        $testTemplate->fromArray($templateData);
        $testTemplate->save();
        $testView = new Xmlteam_ZFView(); 
        $testView->setScriptPath('./application/views');
        $content = $testView->render('testing-header.phtml');
        $this->assertTrue(file_exists('./application/views/testing-header.phtml'));
        $this->assertEquals($content, $templateData['content']);
        $testTemplate->delete();
        unlink('./application/views/testing-header.phtml');
    }   
}
{% endcodeblock %}
For those wondering, yes all the tests pass. ;)</p>
<p>The "Template" is a Doctrine (1.2) model that represents the table where I'm storing information about the templates.  Yes, it has unit tests too.  That pass.
</p>
<p>So how do we accomplish this?  First, I hit up my peeps on Twitter and the advice from <a href="http://twitter.com./weierophinney">Matthew Weier-O'Phinney</a> himself was to simply create my own Zend_View and override what needed to be overriden.   Also, he was very wise to tell me to look at Zend/View.php itself for guidance.   That and some helpful messages from exceptions during testing.
</p>
<p>
Here's the initial implementation, for which all tests pass.
{% codeblock lang:php %}
< ?php

// Custom view that reads in templates from the database and
// writes them to the filesystem

class Xmlteam_ZFView extends Zend_View_Abstract
{
    private $_filter = array();
    private $_file = null;

    public function __construct($config = array())
    {
        parent::__construct($config);
    }

    /**
     * Custom method to see if template is in the file system
     * and then load it into memory, write out to the file system
     * if it doesn't
     *
     * @param string $name The script name to precess
     * @return string THe script output
    */
    public function render($name)
    {
        $scriptPaths = $this->getScriptPaths();
        $filename = $scriptPaths[0] . $name;
        
        if (!file_exists($filename)) {
            list($league, $tmp) = explode('-', $name);
            list($templateType, $extension) = explode('.', $tmp);
            $q = Doctrine_Query::create()
                ->select('t.*')
                ->from('Template t')
                ->where('t.league_short_name = ?', $league)
                ->andWhere('t.type = ?', $templateType);
            $q->setHydrationMode(Doctrine_Core::HYDRATE_ARRAY);
            $results = $q->execute();

            if (count($results) > 0) {
                file_put_contents($filename, $results[0]['content']);
            }
        }
        
        // find the script file name using the parent private method
        $this->_file = $this->_script($name);
        unset($name); // remove $name from local scope

        ob_start();
        $this->_run($filename);

        return $this->_filter(ob_get_clean()); // filter output
    }

                    /**
     * Applies the filter callback to a buffer.
     *
     * @param string $buffer The buffer contents.
     * @return string The filtered buffer.
     */
    private function _filter($buffer)
    {
        // loop through each filter class
        foreach ($this->_filter as $name) {
            // load and apply the filter class
            $filter = $this->getFilter($name);
            $buffer = call_user_func(array($filter, 'filter'), $buffer);
        }

        // done!
        return $buffer;
    }

    /**
     * Includes the view script in a scope with only public $this variables.
     *
     * @param string The view script to execute.
     */
    protected function _run()
    {
        if ($this->_useViewStream && $this->useStreamWrapper()) {
            include 'zend.view://' . func_get_arg(0);
        } else {
            include func_get_arg(0);
        }
    }
}
{% endcodeblock %}
So, what did I learn from this process?
<ol>
<li>I needed to create my own private _file and _filter variables to match what exists in  so that if I create any custom filters they can be applied to my custom view *and* to keep compatibility with existing code.</li>
<li>Because the _run method is protected AND abstract, I needed to implement my own _run method in my custom view, or else it would spit out errors.  Even if it doesn't do anything special.</li>
</ol>
</p>
<p>You can see that the logic in my render method is pretty much as I outlined before.  I realize I will take a slight hit the first time we go to load a particular template.  I'm assuming at some point I will want to run a test to see just how long it does take to pull in the template from the database and write it to the file system.  I'm guessing this will not be a serious performance hit, but you never know.  All those file_exists() calls can't be that good for performance,
</p>
<p>
I look forward to seeing other potential solutions to this problem
</p>
