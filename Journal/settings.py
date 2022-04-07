"""
Django settings for Journal project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#!^bbleg!y2%vo(6vd#l(qph&d+nkboh@&3xs_*@e&@qwoj^nu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'
APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT', 'Development')


ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(' ')
#     [
#     'localhost',
#     '127.0.0.1',
#     'journal-n.herokuapp.com',
# ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Journal.web_app',
    'Journal.auth_accounts',
    'Journal.web_posts',
    'annoying',
    'cloudinary'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'Journal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'Journal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = None

if APP_ENVIRONMENT == 'Production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            # 'DATABASE_URL': os.getenv('DATABASE_URL'),
            # 'NAME': os.getenv('DB_NAME'),
            # 'USER': os.getenv('DB_USER'),
            # 'PASSWORD': os.getenv('DB_PASSWORD'),
            # 'HOST': os.getenv('DB_HOST'),
            'NAME': 'd99dg1fuopbuh2',
            'USER': 'pdksotbhrdajas',
            'PASSWORD': '296ae70f8797fab2233c6ed4f15f51ffb841ebf44f5b59638f5ba90823a13d36',
            'HOST': 'ec2-52-30-67-143.eu-west-1.compute.amazonaws.com',
            'PORT': '5432',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'journal_test2',
            'USER': 'postgres',
            'PASSWORD': '1123QwER',
            'HOST': '127.0.0.1',
            'PORT': '5432',

        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

if APP_ENVIRONMENT == 'Production':
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

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_URL = 'login'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'auth_accounts.AppUser'

cloudinary.config(
  cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME', None),
  api_key=os.getenv('CLOUDINARY_API_KEY', None),
  api_secret=os.getenv('CLOUDINARY_API_SECRET', None),
)
