"""
Django settings for bspg project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import shutil
from . import debug

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEV = debug.DEV
DEBUG = debug.DEBUG 

SESSION_COOKIE_AGE = 86400 
SESSION_SAVE_EVERY_REQUEST = True

PROXIES = {}

if DEV:
    from dev_config import *
    from bspg_keys.dev_app_key import *
    if not DEBUG:
        from bspg_keys.dev_auth_key import *
else:
    from prod_config import *
    from bspg_keys.prod_app_key import *
    if not DEBUG:
        from bspg_keys.prod_auth_key import*


ALLOWED_HOSTS = [
        '*',
]

HBP_COLLAB_SERVICE_URL = 'https://services.humanbrainproject.eu/collab/v0/'
HBP_ENV_URL = 'https://collab.humanbrainproject.eu/config.json'
HBP_IDENTITY_SERVICE_URL = 'https://services.humanbrainproject.eu/idm/v1/api'
HBP_MY_USER_URL = 'https://services.humanbrainproject.eu/idm/v1/api/user/me'
HBP_MY_COLLABS_URL = "https://services.humanbrainproject.eu/collab/v0/mycollabs/"

USE_X_FORWARDED_HOST = True

#CSRF_COOKIE_HTTPONLY = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    'sslserver',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bspg',
    'efelg',
    'sitemap',
    'hh_neuron_builder',
    'bsp_monitor',
    'djangobower',
    'social.apps.django_app.default',
    'hbp_app_python_auth',
    ]

MIDDLEWARE_CLASSES = [
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
]


MIDDLEWARE = [
    #'django.utils.deprecation.MiddlewareMixin',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


AUTHENTICATION_BACKENDS = (
    'hbp_app_python_auth.auth.HbpAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_REVOKE_TOKENS_ON_DISCONNECT = True

ROOT_URLCONF = 'bspg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'bspg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Config dir
CONFIG_URL = 'config'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_POOL = os.path.join(BASE_DIR, 'static_pool')

if os.path.exists(STATIC_POOL):
    STATICFILES_DIRS = [
        STATIC_POOL
    ]
else:
    STATICFILES_DIRS = []


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)


if LOGIN_URL == 'https://bspg.pa.ibf.cnr.it/login/hbp/':
    shutil.copyfile(os.path.join(STATIC_ROOT, 'ibf_bspg_analytics.js'), \
            os.path.join(STATIC_ROOT, 'bspganalytics.js'))
elif LOGIN_URL == 'https://bspg.humanbrainproject.eu/login/hbp/':
    PROXIES = {
        "http":"http://bbpproxy.epfl.ch:80/",
        "https":"http://bbpproxy.epfl.ch:80/",
    }
    shutil.copyfile(os.path.join(STATIC_ROOT, 'epfl_bspg_analytics.js'), \
            os.path.join(STATIC_ROOT, 'bspganalytics.js'))

BOWER_COMPONENTS_ROOT = BASE_DIR

BOWER_INSTALLED_APPS = (
    'hbp-collaboratory-theme',
)

#CSRF_COOKIE_SECURE = True
