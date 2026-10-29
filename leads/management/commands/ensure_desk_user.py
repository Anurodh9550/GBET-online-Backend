import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create the admissions desk user from ADMIN_USERNAME and ADMIN_PASSWORD."

    def handle(self, *args, **options):
        username = os.environ.get("ADMIN_USERNAME", "admin").strip()
        password = os.environ.get("ADMIN_PASSWORD", "")
        email = os.environ.get("ADMIN_EMAIL", "admin@gbte.in").strip()
        if not password:
            self.stderr.write("ADMIN_PASSWORD is not set.")
            return
        User = get_user_model()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email, "is_staff": True, "is_superuser": True},
        )
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        verb = "Created" if created else "Updated"
        self.stdout.write(f"{verb} desk user {username}")
