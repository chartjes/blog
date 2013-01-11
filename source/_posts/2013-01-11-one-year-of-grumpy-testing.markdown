---
layout: post
title: "One year of Grumpy Testing" 
author: Chris Hartjes
date: 2013-01-11
comments: true 
sharing: true 
---
It was one year ago today that I released ["The Grumpy Programmer's Guide To Building Testable PHP Applications"](http://grumpy-testing.com). 650+ customers later (about 10% of those are free copies) 
I am happy with some of the outcomes, and unhappy about others.

Just for the sake of openness, here's an awesome ASCII bar graph made with
[barg](https://github.com/stefanschramm/barg) to show you week-by-week sales
counts and numbers. I apologize for the scrolling you might have to do to see it.

<pre>
Week Starting          #  Paid
2012-01-09 00:00:00-05 56 $673.06 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
2012-01-16 00:00:00-05 29 $306.05 |||||||||||||||||||||||||||||||||||||||||                                         
2012-01-23 00:00:00-05 17 $95.00  ||||||||||||||||||||||||                                                          
2012-01-30 00:00:00-05 19 $203.50 |||||||||||||||||||||||||||                                                       
2012-02-06 00:00:00-05 17 $160.00 ||||||||||||||||||||||||                                                          
2012-02-13 00:00:00-05 7  $73.05  ||||||||||                                                                        
2012-02-20 00:00:00-05 14 $162.2  ||||||||||||||||||||                                                              
2012-02-27 00:00:00-05 7  $89.71  ||||||||||                                                                        
2012-03-05 00:00:00-05 6  $69     ||||||||                                                                          
2012-03-12 00:00:00-04 7  $70.93  ||||||||||                                                                        
2012-03-19 00:00:00-04 15 $128.67 |||||||||||||||||||||                                                             
2012-03-26 00:00:00-04 55 $356.97 |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||   
2012-04-02 00:00:00-04 11 $131.00 |||||||||||||||                                                                   
2012-04-09 00:00:00-04 1  $8.50   |                                                                                 
2012-04-16 00:00:00-04 25 $277.30 ||||||||||||||||||||||||||||||||||||                                              
2012-04-23 00:00:00-04 16 $157.83 |||||||||||||||||||||||                                                           
2012-04-30 00:00:00-04 8  $95.00  |||||||||||                                                                       
2012-05-07 00:00:00-04 7  $81.50  ||||||||||                                                                        
2012-05-14 00:00:00-04 8  $75.04  |||||||||||                                                                       
2012-05-21 00:00:00-04 13 $43.00  ||||||||||||||||||                                                                
2012-05-28 00:00:00-04 2  $21.50  ||                                                                                
2012-06-04 00:00:00-04 19 $149.41 |||||||||||||||||||||||||||                                                       
2012-06-11 00:00:00-04 8  $74.42  |||||||||||                                                                       
2012-06-18 00:00:00-04 10 $92.00  ||||||||||||||                                                                    
2012-06-25 00:00:00-04 7  $30.00  ||||||||||                                                                        
2012-07-02 00:00:00-04 11 $104.08 |||||||||||||||                                                                   
2012-07-09 00:00:00-04 14 $157.47 ||||||||||||||||||||                                                              
2012-07-16 00:00:00-04 3  $26.99  ||||                                                                              
2012-07-23 00:00:00-04 3  $34.50  ||||                                                                              
2012-07-30 00:00:00-04 11 $120.50 |||||||||||||||                                                                   
2012-08-06 00:00:00-04 4  $43.00  |||||                                                                             
2012-08-13 00:00:00-04 10 $108.00 ||||||||||||||                                                                    
2012-08-20 00:00:00-04 4  $47.50  |||||                                                                             
2012-08-27 00:00:00-04 7  $82.00  ||||||||||                                                                        
2012-09-03 00:00:00-04 6  $55.50  ||||||||                                                                          
2012-09-10 00:00:00-04 6  $464.98 ||||||||                                                                          
2012-09-17 00:00:00-04 6  $62.01  ||||||||                                                                          
2012-09-24 00:00:00-04 3  $34.50  ||||                                                                              
2012-10-01 00:00:00-04 5  $61.40  |||||||                                                                           
2012-10-08 00:00:00-04 55 $624.92 |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||   
2012-10-15 00:00:00-04 21 $218.78 ||||||||||||||||||||||||||||||                                                    
2012-10-22 00:00:00-04 16 $169.50 |||||||||||||||||||||||                                                           
2012-10-29 00:00:00-04 6  $105.00 ||||||||                                                                          
2012-11-05 00:00:00-05 12 $120.00 |||||||||||||||||                                                                 
2012-11-12 00:00:00-05 4  $43.00  |||||                                                                             
2012-11-19 00:00:00-05 10 $112.02 ||||||||||||||                                                                    
2012-11-26 00:00:00-05 9  $101.25 |||||||||||||                                                                     
2012-12-03 00:00:00-05 15 $159.00 |||||||||||||||||||||                                                             
2012-12-10 00:00:00-05 6  $72.30  ||||||||                                                                          
2012-12-17 00:00:00-05 13 $142.03 ||||||||||||||||||                                                                
2012-12-24 00:00:00-05 4  $38.50  |||||                                                                             
2012-12-31 00:00:00-05 1  $13.90  |                                                                                 
</pre>

What am I disappointed about? I think, to use the old expression, I left a lot
of money on the table. I could've charged more for the book, but this was
before I started learning more about the marketing of info products and
how to do research to find solutions to problems people are experiencing.

Setting that aside, I think my Testing Crusade is paying dividends for the
community as a whole. The more developers who are exposed to the ideas
that people like myself are promoting, the higher quality code that
is likely to be produced.

If you're a customer of mine, thanks so much for supporting my efforts through
your paid contributions. Writing automated tests and code that you can easily test doesn't have to suck.
I can show you how to do it, and I look forward to bringing you more of it
in 2013.

