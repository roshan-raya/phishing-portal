from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class RecipientList(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_lists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class RecipientContact(models.Model):
    recipient_list = models.ForeignKey(RecipientList, on_delete=models.CASCADE, related_name='contacts')
    email = models.EmailField()
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['recipient_list', 'email']
        ordering = ['email']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"