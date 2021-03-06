# -*- coding: utf-8 -*-
# Django settings for complete pinax project.

import os.path
import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
    filename = '/tmp/bme.log',
    filemode = 'w'
)

PINAX_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../pinax"))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# tells Pinax to use the default theme
PINAX_THEME = 'default'

DEBUG = False 
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through django.views.static.serve.
SERVE_MEDIA = True

ADMINS = (
    ('Jeffrey Johnson', 'ortelius@burningman.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'dev.db'       # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

HAYSTACK_SEARCH_ENGINE = 'xapian'
HAYSTACK_SITECONF = 'bme.search_sites'


AVATAR_GRAVATAR_BACKUP=False
AVATAR_DEFAULT_URL='/media/img/man-icon.png'

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Pacific'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "media")

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bk-e2zv3humar79nm=j*bwc=-ymeit(8a20whp3goq4dh71t)s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'dbtemplates.loader.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'piston.middleware.CommonMiddlewareCompatProxy',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_openid.consumer.SessionConsumer',
    'account.middleware.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'misc.middleware.SortOrderMiddleware',
    'djangodblog.middleware.DBLogMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'bme.urls'
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",

    "notification.context_processors.notification",
    "announcements.context_processors.site_wide_announcements",
    "account.context_processors.openid",
    "account.context_processors.account",
    "misc.context_processors.contact_email",
    "misc.context_processors.site_name",
    "messages.context_processors.inbox",
    "friends_app.context_processors.invitations",
    "misc.context_processors.combined_inbox_count",

    "brc.context_processors.bme_production",

    "points.context_processors.ol_media",
    "points.context_processors.GAK",
    "checkins.context_processors.ALLOW_CHECKINS",
)

COMBINED_INBOX_COUNT_SOURCES = (
    "messages.context_processors.inbox",
    "friends_app.context_processors.invitations",
    "notification.context_processors.notification",
)

INSTALLED_APPS = (
    # included
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.markup',
    
    # external
    'notification', # must be first
    'django_openid',
    'emailconfirmation',
    'django_extensions',
    'robots',
    'dbtemplates',
    'friends',
    'mailer',
    'messages',
    'announcements',
    'oembed',
    'djangodblog',
    'pagination',
#    'gravatar',
    'threadedcomments',
    'wiki',
    'swaps',
    'timezones',
    'feedutil',
    'app_plugins',
    'voting',
    'tagging',
    'bookmarks',
    'blog',
    'ajax_validation',
    'imagekit',
    'avatar',
    'flag',
    'schedule',
    'swingtime',
    'microblogging',
    'piston',
    'api',
    # internal (for now)
    'analytics',
    'profiles',
    'account',
    'tribes',
    'projects',
    'misc',
    'photos',
    'tag_app',
    'uni_form',
    'brc',
    'regionals',
    'django.contrib.admin',
    'django.contrib.gis',
    'django.contrib.databrowse',
    'haystack',
    'lost_found',
    'olwidget',
    'points',
    'listings',
    'checkins',
)

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/%s/" % o.username,
}

AUTH_PROFILE_MODULE = 'profiles.Profile'
NOTIFICATION_LANGUAGE_MODULE = 'account.Account'

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG
CONTACT_EMAIL = "playacal-admin@burningman.com"
SITE_NAME = "Burning Man Earth"
LOGIN_URL = "/account/login"
LOGIN_REDIRECT_URLNAME = "what_next"

INTERNAL_IPS = (
    '127.0.0.1',
)

ugettext = lambda s: s
LANGUAGES = (
  ('en', u'English'),
  ('de', u'Deutsch'),
  ('es', u'Español'),
  ('fr', u'Français'),
  ('sv', u'Svenska'),
  ('pt-br', u'Português brasileiro'),
  ('he', u'עברית'),
  ('ar', u'العربية'),
  ('it', u'Italiano'),
)

# URCHIN_ID = "ua-..."

CACHE_BACKEND = "locmem:///?max_entries=3000"
FEEDUTIL_SUMMARY_LEN = 60*7 # 7 hours

class NullStream(object):
    def write(*args, **kw):
        pass
    writeline = write
    writelines = write

RESTRUCTUREDTEXT_FILTER_SETTINGS = { 'cloak_email_addresses': True,
                                     'file_insertion_enabled': False,
                                     'raw_enabled': False,
                                     'warning_stream': NullStream(),
                                     'strip_comments': True,}

# if Django is running behind a proxy, we need to do things like use
# HTTP_X_FORWARDED_FOR instead of REMOTE_ADDR. This setting is used
# to inform apps of this fact
BEHIND_PROXY = False

FORCE_LOWERCASE_TAGS = True

WIKI_REQUIRES_LOGIN = True
PISTON_STREAM_OUTPUT = True
PISTON_DISPLAY_ERRORS = True
PISTON_EMAIL_ERRORS = True
# Uncomment this line after signing up for a Yahoo Maps API key at the
# following URL: https://developer.yahoo.com/wsregapp/
# YAHOO_MAPS_API_KEY = ''

# For bme.burningman.com
GOOGLE_API_KEY =\
        'ABQIAAAABH87p-yQOJj-sh06NusQiRQLpPod3aNACjAAjaNKf9qxH3IW9RQD3Xdlk03aDvbqDqgbZKEnmbv2Kg'

# For 127.0.0.1:8000, put the following in you local_settings.py for dev.
#GOOGLE_API_KEY =\
#        'ABQIAAAABH87p-yQOJj-sh06NusQiRTpH3CbXHjuCVmaTc5MkkU4wO1RRhTdrjDBgVDitkd2sidQwpIj12NE2w'

ALLOW_CHECKINS = True

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
# Template dirs down here because they have to reflect changes in PINAX_ROOT done in local_settings
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    os.path.join(PINAX_ROOT, "templates", PINAX_THEME),
)


import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

BME_PRODUCTION=True
