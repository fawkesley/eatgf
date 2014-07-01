"""
Django settings for eatgf.org, common to all environments.

The policy here is that if a setting is truly environment-specific, such
as DEBUG, we should set it to the most secure option here, and let other
environments override. Sometimes the most secure is not to include it,
like SECRET_KEY

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from os.path import abspath, dirname, join as pjoin
from urlparse import urlparse


BASE_DIR = abspath(pjoin(dirname(__file__), '..'))

sys.path.append(pjoin(BASE_DIR, 'apps'))
sys.path.append(pjoin(BASE_DIR, 'libs'))

SECRET_KEY = os.environ.get('SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'www.eatgf.org',
    'www-staging.eatgf.org',
    'eatgf.herokuapp.com',
    'eatgf-staging.herokuapp.com',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'eatgf.apps.restaurants',
    'eatgf.apps.locations',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eatgf.urls'

WSGI_APPLICATION = 'eatgf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# eg postgres://user3123:pass123@database.foo.com:6212/db982398

if 'DATABASE_URL' in os.environ:
    DATABASE_URL = urlparse(os.environ['DATABASE_URL'])
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DATABASE_URL.path[1:],
            'USER': DATABASE_URL.username,
            'PASSWORD': DATABASE_URL.password,
            'HOST': DATABASE_URL.hostname,
            'PORT': DATABASE_URL.port,
        }
    }
else:
    DATABASES = None

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    pjoin(BASE_DIR, 'static'),
]

TEMPLATE_DIRS = [
    pjoin(BASE_DIR, 'template'),
]
