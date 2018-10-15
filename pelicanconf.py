#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael McGurk'
SITENAME = u'Laptop Biology - Mike McGurk'
SITEURL = 'https://laptopbiologist.github.io'

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = u'English'


#Theme
MARKDOWN = [
    'codehilite(css_class=highlight)',
    'extra',
    'headerid',
    'toc(anchorlink=true)'
]
DEFAULT_CATEGORY = 'Blogs'
USE_FOLDER_AS_CATEGORY = False
USER_LOGO_URL=SITEURL+'/images/your_logo.png'
LANDING_PAGE_ABOUT={"title":"Tackling biological questions with computational approaches",\
"details":"I'm a computional biologist in the sense that I love thinking about "}

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

CATEGORY_URL = 'categories/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL
CATEGORIES_SAVE_AS = 'categories.html'

TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tags.html'

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
SOCIAL = (('Twitter', 'http://twitter.com/laptopbiologist'),
          ('Github', 'http://github.com/laptopbiologist'),
          ('Email','mailto:mpm289@cornell.edu'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


THEME= "C:/git-repos/pelican-themes/elegant"
##THEME= "C:/git-repos/pelican-elegant-1.3/pelican-elegant-1.3"
##PLUGIN_PATHS = ['C:/git-repos/pelican-plugins']
##PLUGIN_PATHS = [u'C:/git-repos/pelican-plugins']
##PLUGINS = [
##    'sitemap',
##    'tipue_search',
##    'extract_toc',
##    'related_posts',
##    'latex',
##    'liquid_tags.img',
##    'share_post',
##    'series',
##    'neighbors'
##]
##PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'post_stats']
##MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'to]
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']