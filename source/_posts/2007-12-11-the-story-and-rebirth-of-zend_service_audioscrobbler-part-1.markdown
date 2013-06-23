--- 
layout: post
title: The Story and Rebirth Of Zend_Service_Audioscrobbler, Part 1
date: 2007-12-11
author: Chris Hartjes
---
<p>
Many moons ago I set out (along with my friend <a href="http://derekmartin.ca">Derek</a>) to make a contribution to <a href="http://framework.zend.com">Zend Framework</a> in the form of an add-on to let people easily access the <a href="http://www.audioscrobbler.net/">Audioscrobbler</a> web service.  We worked really hard, implemented all the features of the web service at that time.  Imagine our surprise when it got accepted as part of the 1.0 release of Zend Framework!  Awesome!  It even has <a href="http://framework.zend.com/manual/en/zend.service.audioscrobbler.html">it's own entry in the manual and everything.</a></p>
<p>
However, I have a confession to make, although it will not come as a surprise to anyone who reads my blog on a regular basis:  the code is a complete piece of shit.  There.  I said it.  How do I know that it's terrible and needs refactoring in a fierce way?  Check out this lovely snippet of code:
{% codeblock lang:php %}
    //////////////////////////////////////////////////////////
    ///////////////////////  USER  ///////////////////////////
    //////////////////////////////////////////////////////////

    /**
    * Utility function to get Audioscrobbler profile information (eg: Name, Gender)
    * @return array containing information
    */
    public function userGetProfileInformation()
    {
        $service = "/{$this->get('version')}/user/{$this->get('user')}/profile.xml";
        return $this->getInfo($service);
    }

    /**
     * Utility function get this user's 50 most played artists
     * @return array containing info
    */
    public function userGetTopArtists()
    {
        $service = "/{$this->get('version')}/user/{$this->get('user')}/topartists.xml";
        return $this->getInfo($service);
    }

    /**
     * Utility function to get this user's 50 most played albums
     * @return SimpleXML object containing result set
    */
    public function userGetTopAlbums()
    {
        $service = "/{$this->get('version')}/user/{$this->get('user')}/topalbums.xml";
        return $this->getInfo($service);
    }
{% endcodeblock %}
It goes on and on and freakin' on like this.  SEVENTEEN methods just for dealing with user stuff.  This is insane.  Going back over the comments when I was building this thing I realized I totally ignored created elegant code and instead just 'banged out something that worked'.  So, I'm going back to the drawing board and are going to refactor this puppy so it makes sense.   First up, let's talk about dealing with users.  Wouldn't it be better if we had something like this:
{% codeblock lang:php %}
public function user($action) {
     $service = "/{$this->get('version')}/user/{$this->get('user')}/{$action}.xml";
     return $this->getInfo($service);
}
{% endcodeblock %}
Now, THAT looks like nice and elegant.  All I have to do is establish the convention on how to connect to various user-related web services.  That's as simple as comments in the file itself.  Now, to replicate what I was doing before, here are how simple the calls could be:
{% codeblock lang:php %}
$zsa = new Zend_Service_Audioscrobbler();
$zsa->set('user', 'chartjes');
$zsa->set('version', '1.0');
$userProfile = $zsa->user('profile');
$userTopArtists = $zsa->user('topartists');
$userTopAlbums = $zsa->user('topalbums');
{% endcodeblock %}
I think I just got rid of something like 200 lines of code...and that's just in the user section.  Clearly, I majorly screwed it up when I did it the first.  Luckily for me, there is built-in testing for all this stuff so I can refactor and test as I go.</p>
