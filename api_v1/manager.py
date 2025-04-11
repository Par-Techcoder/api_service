from django.contrib.auth.base_user import BaseUserManager
import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not extra_fields.get("dob"):
            raise ValueError("Users must provide a date of birth")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Provide a default dob for superuser if not given
        extra_fields.setdefault("dob", datetime.date(2000, 1, 1))

        return self.create_user(email, password, **extra_fields)
