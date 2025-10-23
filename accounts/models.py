from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        INSTRUCTOR = "INSTRUCTOR", "Instructor"
        RECIPIENT = "RECIPIENT", "Recipient"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.RECIPIENT,
        db_index=True,
    )

    def is_admin(self):
        return self.role == self.Roles.ADMIN or self.is_superuser

    def is_instructor(self):
        return self.role == self.Roles.INSTRUCTOR

    def is_recipient(self):
        return self.role == self.Roles.RECIPIENT
