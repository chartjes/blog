--- 
layout: post
title: "You Asked For It:  Chris' Awesome But Short Guide To Deployment Using Phing"
---
<p>I have been suffering from a major case of blogger's block, so I reached out to the lucky people who follow me on Twitter to ask them about some topics to talk about on the blog.  Thanks to them I've got at least two blog posts coming.  Credit to this one goes to Neil Crookes (who I met at the first CakeFest conference in Orlando) who suggested I talk about <a href="http://twitter.com/neilcrookes/status/12119140914">deployment issues</a>
</p>
<p>What's that you are saying?  You thought I was using <a href="http://capify.org">Capistrano</a> to do deployments at work?  Gentle reader, things change.  All my work in trying to automate deployments is designed to allow me to do a deployment either from my own laptop or remotely on the server where it's run.  Tools like Capistrano and <a href="http://phing.info">Phing</a> let me do that.  Sure, I could cobble together my own solution using rsync or shell scripts, but my experience telecommuting has taught me that if you want others to use your tools, they have to be tools that can be used by others.
</p>
<p>While Capistrano is certainly up to the task of deploying my own personal projects, I had nothing but problems getting people OTHER than myself to get it up and running.  You wouldn't think that getting Ruby and then assorted gems installed on a non-Windows machine would be that hard.  Apparently it is.  So what was my alternate solution?  Create something that can be run on the server where the code is going to be deployed.
</p>
<p>
As a guy who is always up to his neck in the <a href="http://www.jedi.be/blog/2010/02/12/what-is-this-devops-thing-anyway/">devops environment</a> (with a tip of the hat to <a href="http://twitter.com/brianlmoon">Brian Moon</a> for bringing this term to my attention) I am determined to NOT be the only one who can do deployments.  It's 2010, the year we make contact, and there is no reason that my boss, when he alters some marketing copy on our main web site, should not be able to push those changes himself (with the side-effect being leaving me out of it).  With a little work and some digging, I got Phing to do it for me.
</p>
<p>
Like many awesome tools with lots of documentation, Phing suffers from a lack of easy-to-find tutorials covering the exact things I wanted to do.  Or sure, I eventually tracked it all down (with the help of the best support group in the world, Twitter) but I'm guessing this a trend that will not go away.
</p>
<p>
So, being the lazy sort, I set out to duplicate how Capistrano does their deploys:
<ol>
<li>Check out the latest version of code from HEAD on your repo (SVN in this case)</li>
<li>Create a new "current" directory</li>
<li>Symlink the latest checkout (which is in release/yyyymmddhhmmss) to current</li>
</ol>
There are some other steps in here that I use as well that are specific to my applications but these are the basics.
</p>
<p>Why the symlink method?  Capistrano allows you to also rollback to a previous deployment, but I haven't gotten around to implementing that feature with the new Phing-based setup.  I never make mistakes that need to be rolled back like that.  Yes, I'm kidding.
</p>
<p>So, what would a build script to cover the basics look like?
{% codeblock lang:xml %}
< ?xml version="1.0"?>                                                                               
<project name="build" default="main">
    <property name="exportdir"  value="/var/www/foo" />
    <property name="svnpath" value="/usr/bin/svn" />
    <property name="repo" value="REDACTED" />
    <tstamp>
        <format property="build.time" pattern="%Y%m%d%H%I%S" />
    </tstamp>
    <target name="main" depends="svnexport">
        <exec command="rm -f ${exportdir}/current" escape="false" />
        <exec command="ln -s ${exportdir}/releases/${build.time} ${exportdir}/current" escape="false" />
    </target>
    <target name="svnexport">
        <svnexport svnpath="${svnpath}"
            nocache="true"
            repositoryurl="${repo}"
            todir="${exportdir}/releases/${build.time}"/>
    </target>
</project>
{% endcodeblock %} 
I know there are XML haters out there, but that's a readable configuration file right there.  One of the things I did was to remove any user name and password information from the config file.  You never know if you'll get cracked by a script kiddie exploit and someone reads a configuration file full of critical information.  Call me paranoid, butyaneverknow.
</p>
<p>
So, after you install Phing then to run things you just need to type 'phing -f <path to deploy file>'.  In our case, I then get prompted for a password, as the user names on the servers are the same as for the SVN repo.
</path></p>
<p>So what else do I do when I deploy?  There is always some clean-up work to be done after the fact, so I add a few more actions to the file:
{% codeblock lang:xml %}
        <exec command="chmod -R 777 ${exportdir}/current/tmp" escape="false" />
        <exec command="chown -R user:group ${exportdir}/current" escape="false" />
        <exec command="chmod -R ug+rw ${exportdir}/current" escape="false" />
{% endcodeblock %} 
I won't get into the details of what I'm doing there, but you can execute any command you want on the server, so long you have permissions to do so. 
</p>
<p>So, sometimes you are lazy and don't want to mess around with symlinks and figuring out how to roll things backwards.  Here's how you could do a deployment using Phing that simply updates a directory that you checked out using SVN already:
{% codeblock lang:xml %}
< ?xml version="1.0"?>
<project name="build" default="main">
        <property name="svnpath" value="/usr/bin/svn" />
        <property name="username" value="codemonkey" />
        <property name="exportdir"  value="/var/www/bar" />
        <target name="main" depends="svnupdate" />
        <target name="svnupdate">
                <svnupdate svnpath="${svnpath}"
                        username="${username}"
                        nocache="true"
                        todir="${exportdir}"/>
        </target>
</project>
{% endcodeblock %} 
Again, very straight-forward.  Phing is a very powerful tool that can be used for a lot more than just deployments.  Browsing through the documentation gave me some ideas for extending Phing further to meet our deployment needs.  If you deal with PHP all the time, I cannot think of a better tool to help with complex build-and-deploy tasks than Phing.  
</p>
