# community/models.py

from django.db import models
from users.models import CustomUser
from django.utils import timezone

class CommunityPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_global = models.BooleanField(default=True)

class CoursePost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_global = models.BooleanField(default=False)
