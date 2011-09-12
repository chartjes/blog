--- 
layout: post
title: Zend_Service_Audioscrobbler Update
---
<p>In my spare time I've been banging away at writing the required unit tests for the <a href="http://framework.zend.com/wiki/display/ZFPROP/Zend_Service_Audioscrobbler+Proposal+-+Chris+Hartjes,+Derek+Martin">Zend_Service_Audioscrobbler</a> component that <a href="http://derekmartin.ca">Derek</a> and I had started.  I finished all the unit tests for the user based functions, which is a nice milestone.  Then I decided to go back and actually read the comments made from the proposal.  Oops.  I discovered there were a bunch of changes that the folks at Zend said needed to be made in order to accept them.  I agree with most of them.  To save you the trouble of scrolling all the way to the bottom, here they are:
</p>


<blockquote>
Zend Comments

The proposal is approved on the condition that the following issues are addressed by the proposal author.

Public properties make the set* methods redundant. Ideas for resolution:

    * Change the properties to be protected and using the existing set* methods along with new corresponding get* methods.
    * Override __get() and __set(), storing properties in a protected array.

Another option would be to pass the "properties" as method arguments:

< ?php
$as = new Zend_Service_Audioscrobbler();
$profileInfo = $as->userGetProfileInformation('BigDaddy71');
$relatedArtists = $as->artistGetRelatedArtists('LCD Soundsystem');
// ...
?>

No underscores within variable names and compliance with other coding standards.

What is the reason that setDate() and getInfo() methods are designated private? Should they not be inherited and accessible by subclasses, and if so, why not?

We should leverage Zend_Date as it becomes available for date-specific operations.

How do Zend_Service_Audioscrobbler and the Audioscrobbler web services support limiting the number of records returned by a request?

The API presented causes extra effort to programmatically select functionality, due to the practice of essentially embedding options into the method names. Usually function names accept parameters to select between different, related behaviors. For example, the proposal shows:

public function userGetRecentWeeklyArtistChart()
public function userGetRecentWeeklyAlbumChart()
public function userGetRecentWeeklyTrackChart()
public function userGetPreviousWeeklyArtistChart()
public function userGetPreviousWeeklyAlbumChart()
public function userGetPreviousWeeklyTrackChart()

Using class constants having string values we could nicely refactor the above list of methods to something like:

getChart($type, $recent = true)

Similarly, what about:

// source = 'user' | 'artist'
// type = 'artists' | 'albums' | 'tracks' | etc.
getTop($source, $type)
</blockquote>
<p>
All very sensible, so I've got some refactoring work to do.
</p>

