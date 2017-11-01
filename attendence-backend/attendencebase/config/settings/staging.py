from .base import *

SITE_ADDRESS = 'http://moviebase.southindia.cloudapp.azure.com/'

MEDIA_ROOT = str(BASE_DIR + '/media')

STATIC_ROOT = str(BASE_DIR + '/static')

STATIC_URL = '/static/'

MEDIA_URL = '/media/'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': get_secret('DATABASE_NAME'),
        'USER': get_secret('DATABASE_USER'),
        'PASSWORD': get_secret('DATABASE_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',  # you can change this like: DATABASES['default']['PORT'] = 'some_other_port'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
    'applogfile': {
        'level':'DEBUG',
        'class':'logging.handlers.RotatingFileHandler',
        'filename': '~/logs/moviebase-backend.log',
        'maxBytes': 1024*1024*15, # 15MB
        'backupCount': 10,
    },
}
