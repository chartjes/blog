---
layout: post
title: "Tricorder: a testing helper for PHP" 
author: Chris Hartjes
date: 2012-05-31
comments: true 
sharing: true 
---
I've hacked together a little CLI script that I think will be of use to many
people who are trying to answer the question "just what should I do to test
this thing anyway?" as they learn how to write PHPUnit tests to go along with
their code.

While I as at php|tek 2012 I had a conversation with [Michelangelo van Dam](https://twitter.com/DragonBe)
about an idea I had for a testing tool: something that could look at your code
and give you suggestions on what you should be testing. In no time flat he
hooked me up with one of the core guys on the [phpDocumentor](http://phpdoc.org) project,
[Mike van Riel](https://twitter.com/mvriel) and in the course of one short Skype
chat I knew I had the right tools for the job.

I've created something that I am calling [PHP-Tricorder](https://github.com/chartjes/php-tricorder/), a CLI
utility that can be used in conjunction with phpdoc structure.xml files to make
suggestions on testing scenarios. It's at a 0.1 release right now, so I anticipate
it will grow and add more features as time goes on. I'd like to think right now
that it's pretty useful for people who are just beginning down the road of
writing tests for their code.

Here's some sample output from a run of PHP-Tricorder:

    chartjes@php-vm:~/php-tricorder$ php tricorder.php ../building-testable-applications/lib/IBL/structure.xml 
    Reading in phpDocumentor structure file...

    FranchiseMapper.php

    Scanning FranchiseMapper

    __construct -- make sure to mock $conn as \PDO

    createFranchiseFromRow -- make sure to test $row using an empty array()

    delete -- make sure to mock $franchise as \IBL\Franchise

    findAll -- make sure to test method returns \IBL\Franchise instances
    findByConference -- make sure to test $conference using null or empty strings

    findByConferenceDivision -- make sure to test $conference using null or empty strings

    findByNickname -- make sure to test $nickname using null or empty strings

    findById -- make sure to test $id using non-integer values

    generateMap -- make sure to test $teamsTable using null or empty strings

    save -- make sure to mock $franchise as \IBL\Franchise

    _insert -- non-public methods are difficult to test in isolation
    _insert -- make sure to mock $franchise as \IBL\Franchise

    _update -- non-public methods are difficult to test in isolation
    _update -- make sure to mock $franchise as \IBL\Franchise

So check the project out on Github, pull requests and patches are welcome
and I look forward to building this tool out to meet the needs of other
PHP developers.
