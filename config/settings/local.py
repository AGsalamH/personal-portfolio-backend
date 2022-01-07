from .base import *

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']


# django_debug_toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# Media
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = 'static/'
