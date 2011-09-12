--- 
layout: post
title: More Awesome Deployment Using Phing
---
<p>In a previous blog post I showed some very basic techniques for using Phing for doing deployment.  As with any good deployment process, once you let people know that there is a flexible deployment tool other people start asking you to new things.</p>
<p>
"Hey Chris, can you set things up so that whenever someone runs one of those deployment scripts, we send an email to our support mailbox of all the files that were pushed up since the last deploy?"  After pausing for a minute to figure out how I would do it (the quick answer was "no idea") I said "Sure, I'll see what I can do."
</p>
<p>
So I stood in front of my whiteboard and proceeded to sketch out an idea of how I would want to do such a thing.  Luckily I could cheat and look at how Capistrano did it.  Because the way that they do it makes so much sense, so I duplicated it quick-and-dirty style.  A big thanks goes out to my friend <a href="http://www.derekmartin.ca/">Derek</a> for pointing me in the right direction.
</p>
<p>
So, the way to make this happen is as follows:
<ol>
<li>Read in a file inside your current deployment that contains the date of your last deployment</li>
<li>Check your code out of your version control system into <app ROOT>/releases/<date format></date></app></li>
<li>Symlink <app ROOT>/releases/<date format> to <app ROOT>/current</app></date></app></li>
<li>Write a file into <app ROOT>/current that contains the date of the last deploy.
</app></li></ol>
</p>
<p>Here's what it looks like as a Phing script</p>
{% codeblock lang:xml %}
<?xml version="1.0"?>                                                                               
<project name="build" default="main">
    <property name="exportdir"  value="/var/www/app" />
    <property name="svnpath" value="/usr/bin/svn" />
    <property name="repo" value="svn+ssh://path/to/repo" />
    <tstamp>
        <format property="build.time" pattern="%Y%m%d%H%I%S" />
        <format property="newdeploy.date" pattern="%Y-%m-%d %H:%I:%S" />
    </tstamp>
    <property file="${exportdir}/current/deploy.properties" />
    <target name="main" depends="svnexport">
        <exec command="rm -f ${exportdir}/current" escape="false" />
        <exec command="ln -s ${exportdir}/releases/${build.time} ${exportdir}/current" escape="false" />
        <exec command="chmod -R 777 ${exportdir}/current/tmp" escape="false" />
        <exec command="chown -R scriptkiddie:company ${exportdir}/current" escape="false" />
        <exec command="chmod -R ug+rw ${exportdir}/current" escape="false" />
        <exec command="echo 'deploy.date=${newdeploy.date}' >> ${exportdir}/current/deploy.properties" />
        <exec command="svn log -r '{${deploy.date}}':'{${newdeploy.date}}' ${repo} | mail -s 'Deployment Of FizzBuzz in production' support@fizzbuzz" />
    </exec></target>
    <target name="svnexport">
        <svnexport svnpath="${svnpath}"
            username="${username}"
            password="${password}"
            nocache="true"
            repositoryurl="${repo}"
            todir="${exportdir}/releases/${build.time}"/>
    </target>
</project>
{% endcodeblock %}
<p>The key was figuring out the best way to send SVN log information via email.  Leave it to the UNIX way of piping output to provide with the best solution totally within Phing.
</p>
