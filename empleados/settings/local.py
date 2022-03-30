from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'Empleados',
        'USER': 'soyraul',
        'PASSWORD': 'soyraul',
        'HOST': '147.182.130.164',
        'PORT': '5432',

    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child('static')]

MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR.child('media')
