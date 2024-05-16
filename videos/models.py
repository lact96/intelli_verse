# videos/models.py

from django.db import models
from users.models import CustomUser
from django.utils import timezone

class VideoPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_academy_post = models.BooleanField(default=False)
