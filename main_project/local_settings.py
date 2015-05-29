# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  

import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ec2_deploy_test',
        'HOST': 'localhost',
        'USER': 'ec2_deploy_test',
        'PASSWORD': 'cccpussr'
    }
}

# Base dir is up two levels
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# static file dir will live in base dir after collect static is run
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
