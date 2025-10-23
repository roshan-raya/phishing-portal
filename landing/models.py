from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class LandingPage(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content_html = models.TextField()
    indicators = models.JSONField(default=list, blank=True)  # List of phishing indicators
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='landing_pages')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.slug})"