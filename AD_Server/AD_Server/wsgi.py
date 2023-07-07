<<<<<<< HEAD
"""
WSGI config for Global_AD_Server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

=======
>>>>>>> origin/eojin-branch
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AD_Server.settings')

<<<<<<< HEAD
application = get_wsgi_application()
=======
application = get_wsgi_application()
>>>>>>> origin/eojin-branch
