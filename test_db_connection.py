import django
import os

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')
django.setup()

from django.db import connections

def test_connection():
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT 1")
            print("Connection successful:", cursor.fetchone())
    except Exception as e:
        print("Error:", e)

test_connection()
