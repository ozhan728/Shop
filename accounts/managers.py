from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, full_name, password):
        """
        Creates and saves a User with the given phone number and password.
        """
        if not phone_number:
            raise ValueError("Users must have an Phone Number")

        if not email:
            raise ValueError("Users must have an Email")

        if not full_name:
            raise ValueError("Users must have a Name")

        user = self.model(phone_number=phone_number, email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, full_name, password):
        user = self.create_user(phone_number=phone_number, email=email, full_name=full_name, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
