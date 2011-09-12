--- 
layout: post
title: Next-Gen Work Projects
---
<p>We are contemplating the next generation of our <a href="http://www.xmlteam.com/feedfetcher.php">XML feed processing applicatioin</a> and discussing what technologies we want to use.  Personally, I was pushing for <a href="http://twistedmatrix.com">Twisted</a> because of it's support for concurrency and, well, it's Python.  The main dev on the project (it is currently a Perl application) likes Java, as does our sysadmin (who also updated some existing infrastructure to use Java).  At one time I thought that we could replace some existing Ruby code in our system with some <a href="http://www.jython.org/">Jython</a> code, but like many things I have not been able to free up the time to work on it.
</p>
<p>Since we seemed determined to use Java, I decided to see if I could pique the Java boyz interests and suggested that we take a look at <a href="http://www.scala-lang.org/">Scala</a>.  It's terse, totally object-oriented and has full interoperability with Java itself.  Which, hopefully, means that some of the libraries available for Java that would be of use to our project could be used within Scala as well.
</p>
<p>
See, I'm stuck between a rock and a hard place here:  I'd love to be involved in this project because Scala seems cool, and I've never done any work with Java before.  But will I ever get the chance, being the main web-app guy at work now?  *sigh*
</p>
<p>
I guess I could always go into stealth mode and see if I could whip together a quick prototype using Twisted, just to see if it could connect to our systems and pull down documents.  Hrm...HRM....MUAHAHAHAHAHAHAHAHAHAH.  Time to see if all the comments people made in my Twisted (web) vs. Tornado post are true, and that Twisted is a viable option for pulling in XML documents and parsing them so they fit into a relational database, like our existing product.  It could also be a good excuse to stretch out the use of <a href="http://exist.sourceforge.net">eXist</a> and store documents in that.
</p>


