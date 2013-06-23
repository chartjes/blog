---
layout: post
title: "First steps in Node testing" 
author: Chris Hartjes
date: 2012-10-15
comments: true 
sharing: true 
---
As I've been promising, I wanted to share my thoughts as I am starting to
brush up on my JavaScript and learn how to do something non-trivial with
<a href="http://nodejs.org">Node.js</a>. Of course, I want to use tests to
help me drive my work, and also as a way to keep me focused on small iterations
of work.

I am intending to write some code to act as an API for the <a href="http://www.ibl.org">site that runs my simulation baseball league</a>
and refactor the existing PHP code to consume that API instead of speaking
to the database through CakePHP (really OLD CakePHP at that too) models.

So, it took me a while to search around and find enough information to create
my first integration test. In the end, the stack is <a href="http://visionmedia.github.com/mocha/">Mocha</a>
to do the testing, with <a href="https://github.com/visionmedia/supertest">SuperTest</a> to handle
all the HTTP testing.

So, the app itself is built on <a href="http://expressjs.com/">Express</a> and 
talking to a Postgres database using <a href="https://github.com/brianc/node-postgres">node-postgres</a>.
It seemed to me that express was the best solution for a newcomer to Node but
familiar with MVC / modern web application paradigms.

So, let's take a look at some of the code:

{% codeblock lang:js %}
// Front controller for our API

var application_root = __dirname;
var express = require("express");
var path = require("path");
var pg = require('pg');
var app = express();
var model = require('./transactionmodel');

// Create our database connection
var connectionString = "pg://chartjes:@localhost:5432/ibl_stats";

pg.connect(connectionString, function(err, client) {
  if (err) {
    console.log(err);
  }
});
var client = new pg.Client(connectionString);
var tm = new model.TransactionModel(client);

// Config things we need to get the app going
app.configure(function() {
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
  app.use(express.static(path.join(application_root, "public")));
  app.use(express.errorHandler({ dumpExceptions: true, showStack: true }));
});

app.get('/transactions/archived', function(req, res) {
  var done = function (err, transactions) {
    if(err) {
      res.send("Error querying transactions", 500);
    } else {
      res.send(transactions);
    }

  };

  var currentTransactions = tm.getArchived(done);
});

app.get('/transactions/current', function(req, res) {
  var done = function (err, transactions) {
    if(err) {
      res.send("Error querying transactions", 500);
    } else {
      res.send(transactions);
    }
  };

  var currentTransactions = tm.getCurrent(done);
});

module.exports = app;
{% endcodeblock %}

I am also using the awesome <a href="http://postgresapp.com/">Postgress.app</a>
while working on this app on my laptop.

One of the things I learned while I started to build my tests was that if I
wanted to test stuff in isolation, I needed to alter things slightly and
export my Express "app" as a module instead of including the command 
necessary to make it run and listen for requests on a specific port.

Now, I did find some blog posts about how to write integration tests, but
they either wanted to use <a href="http://coffeescript.org/">CoffeeScript</a>
or was using custom modifications to the testing tools. I am not familiar
enough to write stuff like that (not in JavaScript anyway) so out of
frustration I looked at the source code of Express since <a href="http://brianstoner.com/blog/testing-in-nodejs-with-mocha/">this blog post</a>
mentioned how he created a custom version of something used to help in 
testing.

When I looked at the source of Express, the author had replaced a bunch
of stuff with code that simply imported SuperTest. I think I swore
really loudly at myself for not looking sooner.

Armed with the knowledge that I had my missing piece for the integration
test, I wrote a simple one.

{% codeblock lang:js %}
var app = require('../app');
var request = require('supertest');
var assert = require('assert');

describe('Transaction API', function() {
  it('GET /transactions/current should return 200', function(done) {
    request(app)
      .get('/transactions/current')
      .expect('Content-Type', /json/)
      .expect(200, done);
  });
});
{% endcodeblock %}

It worked, which is the first step. How about another test? Let's make
sure that if we do that call to /transactions/current and verify that
we are getting back a result we expect

{% codeblock lang:js %}
it('GET /transactions/current should return expected results', function(done) {                                                                    
    var fs = require('fs');                                                     
    var currentData = fs.readFile('./current', 'utf8', function(err, data) {    
      if (err) { throw err; }                                                   
      return data;                                                              
    });                                                                         
    request(app)                                                                
      .get('/transactions/current')                                             
      .expect(currentData, done);                                               
  });                     
{% endcodeblock %} 

For this test, I am reading in a text file that contains, for a known database,
a JSON representation of that data. Then I do a call to my API call, and
compare the result I get back to my fixture. Just like any test I would 
write in PHP. Compare the expected to the actual.

In <a href="http://devhell.info/post/2012-10-06/the-grace-hopper-rape-whistle/">episode 21 of /dev/hell</a>
I talked a bit about how I felt that testing skills from one language are
transferrable to another. I think the fact that once I figured out that SuperTest
was the missing tool, it took me less than 30 minutes to write those two tests.
That includes research time reading the documentation for both Mocha and SuperTest.

More tests are sure to come, but I think I've found the right set of tools
for the time being. 
