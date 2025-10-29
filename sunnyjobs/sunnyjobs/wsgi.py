"""
WSGI config for sunnyjobs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
path = '/home/maheshproject/jobs_repo/sunnyjobs'
if path not in sys.path:
    sys.path.append(path)
    os.chdir(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sunnyjobs.settings')
import django
django.setup()
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sunnyjobs.settings')

application = get_wsgi_application()
https://github.com/Ahwankeshari01/jobs_repo.git
