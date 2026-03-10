import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saleZen.settings')

# Vercel-এর জন্য 'app' ভেরিয়েবলটি গুরুত্বপূর্ণ
app = get_wsgi_application()