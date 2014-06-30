from .common import *

if SECRET_KEY is None:
    SECRET_KEY = 'insecure-secret-key-only-for-development'

if 'true' == os.environ.get('DEBUG', 'true'):  # default on but allow disabling
    DEBUG = TEMPLATE_DEBUG = True  # SECURITY WARNING: insecure! leaks secrets.

if DATABASES is None:
    print("Using SQLite database.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
