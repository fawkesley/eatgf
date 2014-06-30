from __future__ import unicode_literals

from django.core.validators import RegexValidator

STRICT_SLUG_RE = r'[a-z0-9-]+'
STRICT_SLUG_VALIDATOR = RegexValidator(
    STRICT_SLUG_RE,
    'Only lowercase alphanumeric characters and hyphens are allowed.')
