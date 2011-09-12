--- 
layout: post
title: "Don't Fear The Command Line: Using CakePHP Shells"
author: Chris Hartjes
date: 2008-09-04
---
<p>
(Note: this is a reposting of an entry I made when trying out <a href='http://habariproject.org'>Habari</a> as my blog software.  If you missed it, I hope you enjoy it now.</p>
<p>
For a consulting job I'm working on where I'm porting a spaghetti-PHP application over to using CakePHP I am moving their existing authorization system over to using Cake's Auth component.  Of course, they are storing all their passwords in plaintext in the user account table, so I needed an easy way to convert all the existing passwords over to be encrypted using the same hash that Auth would use.  Doing this was surprisingly easy thanks to the power of <a href="http://book.cakephp.org/view/110/Creating-Shells-Tasks">shells and tasks in CakePHP.</a>.
</p>
<p>
{% codeblock lang:php %}
/**
 * Shell for encrypted naked passwords with the correct hash for use
 * with the Auth component
 *
 * @auth Chris Hartjes
 */
class EncryptPasswordsShell extends Shell {
	var $uses = array('UserClient');
	
	function main() {
		App::import('Core', 'Security');
		$this->out("Starting to encrypt passwords\n\n");
		$this->UserClient->recursive= -1;
		$users = $this->UserClient->find('all');
		
		foreach ($users as $user) {
			$userName = $user['UserClient']['username'];
			$password = $user['UserClient']['password'];
			
			if ($password != '') {
				$data = array('UserClient' => array(
					'id' => $user['UserClient']['id'],
					'password' => Security::hash($password, null, true))
				);
				
				if ($this->UserClient->save($data)) {
					$this->out("Updated password for {$userName}");
				}
			} else {
				$this->out("Bad password for {$userName}");
			}
		}
	}
}
{% endcodeblock %}
</p>
<p>
I think the code in there is pretty self-explanatory.  The only "gotcha" I ran into (fixed by a look at the Auth component itself) was that I needed to tell Security::hash() that I wanted to use the salt I defined in my config file.  By default that parameter is set to false, hence the need to explicitly set it to true.
</p>
<p>
Thank to <a href="http://mark-story.com/">Mark Story</a> for pointing me in the right direction for this.</p>
