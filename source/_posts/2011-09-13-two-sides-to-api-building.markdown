---
layout: post
title: Two Sides to API Building
author: Chris Hartjes
date: 2011-09-13
comments: true 
sharing: true 
---
I've been spending a lot of time lately building APIs for projects at work. One is a SOAP API and the other an RPC API (no, not full REST but it is aware of GET vs. POST for certain RPC calls). One of them was built to support an internal project (server-side component for a JS-powered online store) while the other is to help a 3rd party extract data from our own services for integration into their own. Building both of these led me to the epiphany (maybe obvious to you but not to me) that there are really two sides to an API. They are not necessarily the sides you are expecting.

One reason to build an API is to expose data that is in your system. If you're really forward-thinking, you wrote the API first and then your applications follow the form of a [Service-Oriented Architecture](http://en.wikipedia.org/wiki/Service-oriented_architecture). That is the sweet spot for a lot of applications and I cannot lie when I say I want to move some of the infrastructure towards that, but I am drifting off topic. This is the most common form of an API -- you select the data you wish to expose to other people. The advanced version of this, which is essential to building an SOA, is to then allow users to do actions via the API that create, update, or delete data in your system.

The second reason to build an API is to allow for integration with other services. Sounds a lot like the first reason for making an API, right? The big difference is that instead of the people building the API (meaning you and/or me) are not in control of what gets exposed. The party doing the integration will be telling you what data they will need exposed. It's a subtle difference but one that I think is important to understand. Under the first scenario, you are in control and (to use a bad cliche) hold the keys to the kingdom, deciding what data gets exposed.

In the second scenario you are not in control and are relying on 3rd parties to tell you what data they need. Depending on the actual relationship between you and the 3rd party, you might have a chance to move this scenario back to the first one. Keep this in mind next time you are building an API and adjust your expectations accordingly.
