from django.contrib import admin
from .models import CommunityPost, CoursePost

admin.site.register(CommunityPost)
admin.site.register(CoursePost)