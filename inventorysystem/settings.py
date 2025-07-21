"""
Django settings for inventorysystem project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import certifi

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#dtrctd5@x*+)v52#9lry*(1&0qkgt5h3hzzcyhi@#2$$6=k7s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['barcode-driven-inventory-system.onrender.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'products',
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

ROOT_URLCONF = 'inventorysystem.urls'

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

WSGI_APPLICATION = 'inventorysystem.wsgi.application'

# Database
# Remove SQLite if using MongoDB exclusively
DATABASES = {}

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

from mongoengine import connect
connect(
    db=MONGO_DB_NAME,
    host=MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where(),  # Use certifi for SSL certificate validation
    # serverSelectionTimeoutMS=600000,  # 60-second timeout for server selection
    # socketTimeoutMS=60000,  # 60-second timeout for socket operations
    # connectTimeoutMS=60000,  # 60-second timeout for initial connection
    # heartbeatFrequencyMS=2000000,  # Heartbeat every 20 seconds
    # retryWrites=True,  # Retry writes on failure
    # maxPoolSize=50,  # Limit connection pool size
)

# Logging for debugging MongoDB connection issues
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',
#         },
#         'mongoengine': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#         'pymongo': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
# }

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'