from pathlib import Path
from .base import *

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

def get_sql_queries_log_file_path():
    BASE_DIR = Path(__file__).parents[2]
    sql_queries_log_file_path = BASE_DIR / 'sql_queries.log'
    sql_queries_log_file_path.touch()
    return str(sql_queries_log_file_path)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'sql_queries_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': get_sql_queries_log_file_path(),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'qinspect': {
            'handlers': ['sql_queries_handler'],
            'level': 'DEBUG',
            'propagate': True
        }
    },
}