"""
WSGI config for ref_WebApplication project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('\a293491-DevSecOps-Project\ref_WebApplication\VolvoVehicleOrder')
sys.path.append('\a293491-DevSecOps-Project\Lib\site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ref_WebApplication.settings")

application = get_wsgi_application()
