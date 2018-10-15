#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael McGurk'
SITENAME = u'Laptop Biology - Mike McGurk'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = u'English'


#Theme
USER_LOGO_URL=SITEURL+'/images/your_logo.png'
LANDING_PAGE_ABOUT={"title":"Tackling biological questions with computational approaches",\
"details":"I'm a computional biologist in the sense that I love thinking about "}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
##LINKS = (('Pelican', 'http://getpelican.com/'),
##         ('Python.org', 'http://python.org/'),
##         ('Jinja2', 'http://jinja.pocoo.org/'),
##         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('<a href="https://twitter.com/LaptopBiologist?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @LaptopBiologist</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


##THEME= "C:/git-repos/pelican-themes/svbhack"
THEME= "C:/git-repos/pelican-themes/elegant"