"""
WSGI config for tst_36b84c42_aa74_4f7a_87 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_36b84c42_aa74_4f7a_87.settings"
)

application = get_wsgi_application()
