# myproject/production.py
from .settings import *


DEBUG = False
ALLOWED_HOSTS = ['.azurewebsites.net']  # Add your Azure domain

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of your middleware
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
