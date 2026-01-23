print("DEBUG: Starting the admin creation script...")
import os
import django

# Set the settings module (Replace 'basketball_backend' with your actual folder name if different)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basketball_backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# These will be pulled from Render Environment Variables
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin12345')

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser for {username}...")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully.")
else:
    print(f"Superuser {username} already exists. Skipping.")