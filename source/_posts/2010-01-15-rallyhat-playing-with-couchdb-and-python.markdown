--- 
layout: post
title: "Rallyhat: Playing with CouchDB and Python"
---
<p>Many thanks to <a href='http://twitter.com/janl'>Jan Lehnardt</a> for helping me out via IM to understand some concepts that I was having problems wrapping my mind around.</p>
<p>
Rallyhat is for the most part a programming experiment for me, designed to learn Python *and* produce an web application that is actually usable by someone other than me.  One of the technologies I'm using is <a href="http://couchdb.apache.org/">CouchDB</a> to store things.  I was having some problems getting both <a href="http://code.google.com/p/couchdb-python/">couchdb-python</a> working with permanent views (meaning views stored in CouchDB itself) as opposed to temporary views (meaning views generated in the code).
</p>
<p>
Now, couchdb-python looks to be a nice, simple interface to use.  The problem I found was the documentation is, what's the word I'm looking for?  Lacking.  Since Jan is an amazing teacher, he was patient with me and showed me that I could look at the documentation for couchdb-python via the Python REPL (aka the Python shell).  So, armed with this "how the hell could I not realize this" knowledge I figured out how to use it.  Yet another reason why I'm warming up to Python.  
</p>
<p>It was as simple as starting up the Python shell and then doing the following:
{% codeblock lang:python %}
import couchdb
help(couchdb.client)
{% endcodeblock %}
In there you will find code examples for each method, and then explanations of the parameters for each method.  All you really need in this case.  So I take back what I said about the documentation for couchdb-python being lacking.  I was just looking in the wrong place.
</p>
<p>
So, task #1 was to create the view I needed.  I decided to use Futon, the built-in interface to create my permanent view:
{% codeblock lang:javascript %}
{
   "_id": "_design/searches",
   "_rev": "3-e7f43cfdd5a8ef62ae338bd1f19b3e95",
   "views": {
       "by_user": {
           "map": "function (doc) { emit(doc.user, {'date': doc.date, 'locations': doc.loations});}"
       }
   }
}
{% endcodeblock %}
</p>
<p>This view would then live at http://couchdb.server//rallyhat/_design/searches/_view/by_user is you want to get every doc for every user.  To get just the docs belong to a specific user, you append ?key=<user> to the URL above.  Is that easy to understand or what?  As an aside, I am finding the <a href="http://books.couchdb.org/relax/">online version of CouchDB: The Definitive Guide</a> to be an awesome reference guide (once you remember to actually use it, thanks again Jan). With the view then created, the next step was to create the Python code to read in those views.</user></p>
<p>
{% codeblock lang:python %}
     def get_by_user(self, username):
         my_searches = []
 
         if username:
             for row in db.view('searches/by_user', None, key=username):
                 info = db.get(row.id)
                 locations = json.loads(info['locations'])                                                
                 my_search = {'date': info['date'], 'locations': locations}
                 my_searches.append({'id': row.id, 'date': info['date'],
                                     'locations': locations})
     
         return my_searches
{% endcodeblock %}          
</p>
<p>
With *any* Python library that you use, make sure to see if the author added help files to the package.  You'd be surprised to see what's in there...
</p>
