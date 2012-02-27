---
layout: post
title: "Simple API testing using Behat" 
author: Chris Hartjes
date: 2012-02-26
comments: true 
sharing: true 
---
I've recently started using [Behat](http://behat.org) as my testing framework
of choice. Why? I like the idea of writing tests in a format that is as close
to English as I can get. This also makes it easier for non-technical people
to write tests for you as well, making sure they "have some skin in the game"
as you build out your automated test suite.

I have been trying to push my JavaScript skills lately by first playing around
with Node.js to get a feel for event-driven server-side coding and by trying
to build something semi-useful using [Knockout](http://knockout.js). Knockout
is a client-side Model-View-View-Model framework that promotes four really
good principles: declarative bindings, automatic UI refreshing, dependency
tracking and templating. Check out the documentation on the Knockout web site
for a great explanation of why those are good thigns.

A typical Knockout-out powered site is one where the client-side code talks
to a server-side API. My experimental site for this is one that uses an 
API written in PHP using [Slim](http://slimframework.com). Of course, I cannot
do this without writing some tests. My first set of tests are for the calling
of the API itself.

After working with PHPUnit's "assert that the result matches expectations" 
philosophy, switching to using a behavioural approach has changed how I decide
to approach actually testing something. Let me show you what I mean.

Here's a test for an API call to get our "current" set of transactions, which
is hard-coded in the system to be all trades that have occurred in the past
3 weeks.

{% codeblock %}
Feature: transactions API 

Scenario: 
	Given I call "/transactions/current"
	Then I get a response
	And the response is JSON
	And the response contains more than one transaction
	And the first transaction contains a transaction ID
	And the first transaction contains two teams
	And the first transaction contains a description
{% endcodeblock %}

If you read that out loud it sounds like how you would describe to a co-worker
what you were expecting to happen on an API call, albeit a little more stilted
and formalized.

When you first write a feature like this and then ask Behat to run all the
tests on it, if there is no code to execute a specific step it will give you
the skeleton of code to make it happen. Then it is up to you to implement
the actual code that will make the tests run.

Here's the final product:

{% codeblock lang:php %}
<?php

use Behat\Behat\Context\ClosuredContextInterface,
    Behat\Behat\Context\TranslatedContextInterface,
    Behat\Behat\Context\BehatContext,
    Behat\Behat\Exception\PendingException;
use Behat\Gherkin\Node\PyStringNode,
    Behat\Gherkin\Node\TableNode;

//
// Require 3rd-party libraries here:
//
//   require_once 'PHPUnit/Autoload.php';
//   require_once 'PHPUnit/Framework/Assert/Functions.php';
//

/**
 * Features context.
 */
class FeatureContext extends BehatContext
{
    /**
     * Initializes context.
     * Every scenario gets it's own context object.
     *
     * @param   array   $parameters     context parameters (set them up through behat.yml)
     */
    public function __construct(array $parameters)
    {
        // Initialize your context here
    }

    /**
     * @Given /^I call "([^"]*)"$/
     */
    public function iCall($argument1)
    {
        $client = new Guzzle\Service\Client();
        $request = $client->get('http://local.ibl-delphi' . $argument1)->send();
        $this->response = $request->getBody(true);
    }

    /**
     * @Then /^I get a response$/
     */
    public function iGetAResponse()
    {
        if (empty($this->response)) {
            throw new Exception('Did not get a response from the API');
        }
    }

    /**
     * @Given /^the response is JSON$/
     */
    public function theResponseIsJson()
    {
        $data = json_decode($this->response);

        if (empty($data)) {
            throw new Exception("Response was not JSON\n" . $this->response);
        }
    }

    /**
     * @Given /^the response contains more than one transaction$/
     */
    public function theResponseContainsMoreThanOneTransaction()
    {
        $data = json_decode($this->response);

        if (count($data) >= 1) {
            throw new Exception("Response did not contain more than one transaction");
        }
    }

    /**
     * @Given /^the first transaction contains a transaction ID$/
     */
    public function theFirstTransactionContainsATransactionId()
    {
        $data = json_decode($this->response, true);
        $transaction = $data[0];

        if (!isset($transaction['id'])) {
            throw new Exception("First transaction did not contain a transaction id");
        }
    }

    /**
     * @Given /^the first transaction contains two teams$/
     */
    public function theFirstTransactionContainsTwoTeams()
    {
        $data = json_decode($this->response, true);
        $transaction = $data[0];

        if (!isset($transaction['tradePartner1']) && !isset($transaction['tradePartner2'])) {
            throw new Exception("First transaction did not contain two teams");
        }
    }

     /**
     * @Given /^the first transaction contains a description$/
     */
    public function theFirstTransactionContainsADescription()
    {
        $data = json_decode($this->response, true);
        $transaction = $data[0];

        if (!isset($transaction['description'])) {
            throw new Exception("First transaction is missing a description");
        }
    }
}
{% endcodeblock %}

Notice how Behat uses annotations that describe what type of scenario the
method uses. It also uses regular expressions to extract specific values
that you are wishing to test. Those are typically values inside quotes
in the actual features.

If you are wondering what the skeletons (or stubbs depending on what
terminology you like to use) looked like *before* I wrote code to implement
them, you can simply cut-and-paste the scenario file at the top of this
post into a feature file (don't forget to give a .feature extension) and it
will show you all of them.

I liked this method because it meant I could easily add more tests and
Behat would tell me what code woudl be needed to run it.

So what does the output look like for the test?

{% codeblock %}
-> % bin/behat
Feature: transactions API

  Scenario:                                             # features/transactions.feature:3
    Given I call "/transactions/current"                # FeatureContext::iCall()
    Then I get a response                               # FeatureContext::iGetAResponse()
    And the response is JSON                            # FeatureContext::theResponseIsJson()
    And the response contains more than one transaction # FeatureContext::theResponseContainsMoreThanOneTransaction()
    And the first transaction contains a transaction ID # FeatureContext::theFirstTransactionContainsATransactionId()
    And the first transaction contains two teams        # FeatureContext::theFirstTransactionContainsTwoTeams()
    And the first transaction contains a description    # FeatureContext::theFirstTransactionContainsADescription()

1 scenario (1 passed)
7 steps (7 passed)
0m0.492s
{% endcodeblock %}

I have obviously only scratched the surface of what can be done with Behat.
I myself have questions about how to prevent the FeatureContext.php file, 
which contains all the functionality that drives the tests, from getting
too large. I can also see the lure of endlessly tweaking the scenarios to
reduce the amount of code required to run them all.

What about code-coverage reports? Easily available in PHPUnit but is it
possible using Behat? It's still early days for some of the alternatives to
PHPUnit.
 
The example above is only the first of numerous tests that will be written
for this side project, as it needs to cover displaying archived transactions
to be voted on, user authentication, and the voting process itself.

I think that the BDD approach maps better to a results-oriented methodology
when it comes to testing: you are using real-life scenarios to make sure that
you are getting back the results you are expecting. In the end. that is still
the goal of testing.

