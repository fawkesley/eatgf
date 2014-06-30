from .common import *

import os

STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
STATIC_URL = '/static/'

if os.environ.get('EMERGENCY_DEBUG', 'false') == 'true':
    DEBUG = True
    TEMPLATE_DEBUG = True
