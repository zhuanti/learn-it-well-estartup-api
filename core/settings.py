"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0n537xapk)821+*%ea3jo7zz@dxxg$x=h^%3c!q2(9!ol3$@h)'

# SECURITY WARNING: don't run with debug turned on in production!

# 在本地時使用的連線資訊
# DEBUG = True
# ALLOWED_HOSTS = []

# 在Heroku用的連線資訊
DEBUG = False
ALLOWED_HOSTS = ['learn-it-well-estartup-api.herokuapp.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.parse('postgres://ynzuancxnazqqu:fe850b210541dc452da3889638113db2875237cc8640a2783457259848f830ba@ec2-54-226-18-238.compute-1.amazonaws.com:5432/dcva7o0i9ts64b')
# }


DATABASES = {
    'default': dj_database_url.parse('postgres://ctqccghsrclyok:9432225df32767cb8362ef5c8078b8d2a8508a241516fda698f8e8917175a860@ec2-34-202-66-20.compute-1.amazonaws.com:5432/d4kaq6iu2g0psr')
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# class DB():
#     __host = 'ec2-34-202-66-20.compute-1.amazonaws.com'
#     __user = 'ctqccghsrclyok'
#     __dbname = 'd4kaq6iu2g0psr'
#     __password = '9432225df32767cb8362ef5c8078b8d2a8508a241516fda698f8e8917175a860'
#     __sslmode = 'require'
#
#     #-------------------------
#     # 取得資料庫連線
#     #-------------------------
#     @staticmethod
#     def getConn():
#         conn_string = f'host={DB.__host} user={DB.__user} dbname={DB.__dbname} password={DB.__password} sslmode={DB.__sslmode}'
#         return psycopg2.connect(conn_string)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


