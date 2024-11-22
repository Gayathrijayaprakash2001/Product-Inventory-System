import os
from django.core.asgi import get_asgi_application  # Use get_asgi_application for ASGI

# Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ims_django.settings')

# Create the ASGI application
application = get_asgi_application()
