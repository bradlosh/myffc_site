#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = 'ffcadmin'
SITENAME = 'Faith Family Church'
SITEURL = 'https://myffc.org'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = '/home/brad/projects/pelican/myffc_site/theme_twenty'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

#DIRECT_TEMPLATES=['index', 'categories', 'authors', 'archives']
#PAGINATED_DIRECT_TEMPLATES = ['categories']
		  
DEFAULT_PAGINATION = 3
POST_LIMIT = 10

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# Formatting for dates
DEFAULT_DATE_FORMAT = ('%Y-%m-%dT%H:%M:%SZ')

# Formatting for urls
# ARTICLE_DIR = 'posts'
ARTICLE_URL = "posts/{slug}"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"

ARCHIVES_URL = "posts"
ARCHIVES_SAVE_AS = "posts/index.html"

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

USE_FOLDER_AS_CATEGORY = True

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = ['images',
                'fonts',
                'css',
                'js',
                ]
				
PIWIK_URL='analytics.myff.ch'
# first piwik site is always id 1
PIWIK_SITE_ID=2
