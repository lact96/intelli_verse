# models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_professor = models.BooleanField(default=False)

class ProfessorProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    school_logo = models.ImageField(upload_to='school_logos/', blank=True, null=True)

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    professor = models.ForeignKey(ProfessorProfile, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_subscription = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField()

class Video(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.SET_NULL)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
