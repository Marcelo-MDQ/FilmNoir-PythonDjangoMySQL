from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Postgres
#DATABASES = {  
#   'default': {  
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',  
#     'NAME': 'filmnoir',  
#     'USER': 'postgres',
#     'PASSWORD': '1234',
#     'HOST': 'localhost',
#     'PORT': '5432',
#  }  
# }

# MySql
DATABASES = {  
   'default': {  
     'ENGINE': 'django.db.backends.mysql',  
     'NAME': 'filmnoir',  
     'USER': 'root',
     'PASSWORD': '',
     'HOST': 'localhost',
     'PORT': 3306,
     'OPTIONS': {
        'sql_mode': 'traditional',
        }
   }  
 }




