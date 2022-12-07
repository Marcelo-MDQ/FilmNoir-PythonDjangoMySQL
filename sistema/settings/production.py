from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['filmnoir-mdq.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {  
   'default': {  
     'ENGINE': 'django.db.backends.postgresql_psycopg2',  
     'NAME': 'dcq1tk6ltesf41',  
     'USER': 'codzsrjkdsuhof',
     'PASSWORD': '2cf43caa99475cbdffcee5ec3c91f57cc1182ff2670ecbb2198cb86d9d54bbf9',
     'HOST': 'ec2-3-220-207-90.compute-1.amazonaws.com',
     'PORT': 5432,
   }  
 }
