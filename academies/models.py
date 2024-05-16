# academies/models.py

from django.db import models
from users.models import UserProfile

class Academy(models.Model):
    owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='owned_academy')
    name = models.CharField(max_length=255)
    description = models.TextField()
    approved = models.BooleanField(default=False)

class Professor(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    academies = models.ManyToManyField(Academy, through='AcademyProfessor')

class AcademyProfessor(models.Model):
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    permissions = models.JSONField()
