--- 
layout: post
title: Socket Servers
author: Chris Hartjes
---
A lot of programmers who work with PHP don't even know that you can create shell scripts that run in PHP.  I've used them to pull data from remote servers as part of a work project and are also doing fun things with creating a PHP daemon that runs in the background listening to TCP/IP requests on a specifc port.

Why? I'm writing code that will have to parse the output of a Java client that connects to the <a href=http://www.pa-sportsticker.com/en/index.html>SportsTicker</a> service.  We have plans to create a Flash applet that goes on our forum sites that will present the SportsTicker info in various formats.  SportsTicker spits out XML (which PHP 5 is very good at managing) so my listener simply buffers all the data that comes in and then spits out the XML data to a file that another script will most likely read and modify the info.  I know that Flash can apparantly read in XML data, but who knows if the guy who will be building the Flash component actually knows how to do it.  

Here's a sample of the code I've been working on (not the final version obviously) based on a cool tutorial on the Zend site called <a href=http://www.zend.com/pecl/tutorials/sockets/php>Writing Socket Servers in PHP</a>.
{% codeblock lang:php %}
#!/usr/bin/php
<?php

/**
 * PHP script that acts as a listener for the output from the Java Sportsticker Client
 *
 * @author Chris Hartjes
 */

set_time_limit(0);

$address = '127.0.0.1';
$port = 9600;
$max_clients = 10;
$clients = Array();
$read = Array();
$buffer = "";
$sock = socket_create(AF_INET, SOCK_STREAM, 0);
socket_bind($sock, $address, $port) or die('Could not bind to address');
socket_listen($sock);

while (TRUE) {
    $read[0] = $sock;
    
    for ($i = 0; $i< $max_clients; $i++) {
        if (isset($client[$i]['sock']) && $client[$i]['sock'] != NULL) {
            $read[$i + 1] = $client[$i]['sock'];
        }
    }
    
    $ready = socket_select($read, $write = NULL, $except = NULL, NULL);
    
    if (in_array($sock, $read)) {
        
        for ($i = 0; $i < $max_clients; $i++) {
            
            if (!isset($client[$i]['sock'])) {
                $client[$i]['sock'] = socket_accept($sock);
                break;
            } else if ($i == $max_clients - 1) {
                print "Too many clients";
            }
        }
        
        if (--$ready <= 0) {
            continue;
        }
    }
    
    for ($i = 0; $i < $max_clients; $i++) {
        
        if (isset($client[$i]['sock']) && in_array($client[$i]['sock'], $read)) {
            $input = socket_read($client[$i]['sock'], 1024);
            
            if ($input == NULL) {
                unset($client[$i]);
            }
                      
            $input = trim($input);
            
            // Now, we add info to the buffer
            $buffer .= $input;
            
            // Write the data to a file if we have a closing XML tag
            if (stristr($buffer, '</xml>')) {
                echo $buffer;
                $buffer = "";
            }

        } else {
            if (isset($client[$i]['sock'])) {
                socket_close($client[$i]['sock']);
                unset($client[$i]);
            }
        }
    }
}

socket_close($sock);
?>
{% endcodeblock %}
In just about 80 lines you have a working server that listens for requests on a specific port and spits out the data when it thinks you've reached the end.  Once I get a better handle on the actual info coming from SportsTicker (the server that is supposed to run the Java client is having some Java configuration issues that one of our admins is fixing as I type this) then I'm sure I'll put in some error handling and other exceptions.

I'm not entirely happy with the for loop being used to go through all the connections so perhaps I'll spend some time trying to fix it.  If it turns out that I never have more than one connection at a time then I can probably elminate that loop totally, creating some tighter code.  It's never too early to refactor stuff. :)
