#-*- coding: utf-8 -*-

# Blognajd,
# Copyright (C) 2013, Daniel Rus Morales

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PRJ_PATH = os.path.abspath(os.path.curdir)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.sqlite3', 
        'NAME':     'blognajd_tests',
        'USER':     '', 
        'PASSWORD': '', 
        'HOST':     '', 
        'PORT':     '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Brussels'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PRJ_PATH, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

SECRET_KEY = 'v2824l&2-n+4zznbsk9c-ap5i)b3e8b+%*a=dxqlahm^%)68jn'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'blognajd.tests.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), "..", "templates"),
    os.path.join(os.path.dirname(__file__), "templates"),
)

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    'django.contrib.sessions',
    "django.contrib.sites",
    "django.contrib.sitemaps",
    'django.contrib.messages',
    "django.contrib.comments",

    "django_contactme",
    "django_comments_xtd",
    "django_markup",
    "inline_media",
    "flatblocks_xtd",
    "sorl.thumbnail",
    "tagging",
    "blognajd",
    'blognajd.tests',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "blognajd.context_processors.settings",
)

DEFAULT_FROM_EMAIL  = "Alice Bloggs <alice@example.com>"
SERVER_EMAIL        = DEFAULT_FROM_EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

COMMENTS_APP = "django_comments_xtd"
COMMENTS_XTD_CONFIRM_EMAIL = True
COMMENTS_XTD_SALT = "es-war-einmal-una-princesa-in-a-beautiful-castle"

FORCE_LOWERCASE_TAGS = True # django-tagging

THUMBNAIL_BACKEND = "inline_media.sorl_backends.AutoFormatBackend"
THUMBNAIL_FORMAT = "JPEG"

BLOGNAJD_PAGINATE_BY = 5 # number of stories
BLOGNAJD_TRUNCATE_TO = 40 # number of words
LOGIN_URL = "/"

CONTACTME_NOTIFY_TO = "Your Name <user@example.com>"
CONTACTME_SALT = b'change this, write random chars and special chars'

INLINE_MEDIA_TEXTAREA_ATTRS = {
    'default': {
        'style': 'font: 13px monospace'
    },
}

COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_XTD_CONFIRM_EMAIL = False
