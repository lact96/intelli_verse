from django.contrib import admin
from .models import Course, Lesson, UserProfile

admin.site.register(Course)
admin.site.register(UserProfile)
admin.site.register(Lesson)