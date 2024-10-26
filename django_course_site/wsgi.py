"""
WSGI config for django_course_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Add the parent directory of django_course_site to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'django_course_site'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_course_site.django_course_site.settings')

application = get_wsgi_application()
