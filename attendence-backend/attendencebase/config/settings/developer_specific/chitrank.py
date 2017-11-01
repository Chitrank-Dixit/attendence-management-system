from pathlib import Path

__author__ = 'chitrankdixit'

from ..local import *

DEBUG = True

# Database user: attendencebase-admin pass: liomessi10
# Database name: attendencebase-db



INSTALLED_APPS += ['django_extensions', 'debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']#, 'qinspect.middleware.QueryInspectMiddleware']
SHELL_PLUS = "ipython"

CORS_ORIGIN_ALLOW_ALL = True


# Whether the Query Inspector should do anything (default: False)
QUERY_INSPECT_ENABLED = True
# Whether to log the stats via Django logging (default: True)
QUERY_INSPECT_LOG_STATS = True
# Whether to add stats headers (default: True)
QUERY_INSPECT_HEADER_STATS = True
# Whether to log duplicate queries (default: False)
QUERY_INSPECT_LOG_QUERIES = True
# Whether to log queries that are above an absolute limit (default: None - disabled)
QUERY_INSPECT_ABSOLUTE_LIMIT = 100 # in milliseconds
# Whether to log queries that are more than X standard deviations above the mean query time (default: None - disabled)
QUERY_INSPECT_STANDARD_DEVIATION_LIMIT = 2
# Whether to include tracebacks in the logs (default: False)
QUERY_INSPECT_LOG_TRACEBACKS = True
# Project root (a list of directories, see below - default empty)
QUERY_INSPECT_TRACEBACK_ROOTS = ['/Users/chitrankdixit/Documents/Software_Development/stockroomio/assignment/movie_project/movie-backend/moviebase']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'attendencebase-db',
        'USER': 'attendencebase-admin',
        'PASSWORD': 'liomessi10',
        'HOST': '127.0.0.1',
        'PORT': '5432',  # you can change this like: DATABASES['default']['PORT'] = 'some_other_port'
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'eynimumbaiindia@gmail.com'
EMAIL_HOST_PASSWORD = 'liomessi10'


# to check the makemigrations would work correctly or not
# python manage.py makemigrations --dry-run

# to check which migrations have successfully run
# python manage.py showmigrations

# python manage.py showmigrations --plan

