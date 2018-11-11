.. title: Setting up this site - Part 1
.. slug: setting-up-this-site-part-1
.. date: 2018-10-15 22:03:03 UTC-04:00
.. tags: 
.. category: blogging
.. link: 
.. description: 
.. type: text

I've wanted to set up a research blog for a while now. Over the course of any project you stumble across tricks and tools that you can't really emphasize in publications (due to space or focus considerations), but which would be probably helpful to other researchers. Sure, they end up in the (supplemental) methods, but no one is going to find them. And frankly, the solutions to many of the stumbling blocks I've stumbled upon or the "_Eureka!_"-shouting resolution to tricky concepts are found, not in publications, but in the helpful blog posts other researchers took the time to write and publish. Thanks to the internet, the way we disseminate information as researchers has moved beyond conferences and publications (certainly not an original conclusion), and I want to make an active effort to pay forward some of those private _eurekas_.

But I'm a biologist not a computer scientist by training. I think the last time I tried setting anything up resembling a blog was when I made a MySpace page for my cat back in high school (draw for yourself whatever conclusions arise naturally from that admission). So creating a science blog required a bit of planning and consideration. There were several things I knew I wanted. First, I didn't want to pay for anything. Second, however I set up this blog, I wanted the option of directly generating it from my research notes. The reason is I want to lower the activation energy necessary to communicate an idea (I believe accounting for future laziness is key to productivity). These days, my notes are almost exclusively found in Jupyter notebooks, and I've increasingly relied on [Colaboratory](https://colab.research.google.com/) (which is basically Google Docs, but for Jupyter notebooks). So a format that can be painlessly generated from Jupyter notebooks was a must. Another consideration is where should I host this blog.

Googling around for options answered two questions at once "How do I do this?" and "Where do I host the blog?" with  _[Github Pages](with: https://pages.github.com/)_. As it turns out, GitHub--where I store and version control most of my code--allows users to host (for free) static web pages in a repository titled username.github.io. The restriction that they be static meant that the "How?" probably ought to be something that can generate static web pages. It looked like there were several appealling options, with Jekyll and Pelican being the most commonly recommended. I played with Jekyll and bit a really liked (for great ), but all of the guides for converting Jupyter notebooks to web pages seemed like the process was clunky. So I went with Pelican (which is apparently an anagram of the French for 'notebook': calepin)

