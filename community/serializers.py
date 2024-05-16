# community/serializers.py

from rest_framework import serializers
from .models import CommunityPost, CoursePost
from users.serializers import CustomUserSerializer
from courses.serializers import CourseSerializer

class CommunityPostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = CommunityPost
        fields = ['id', 'user', 'content', 'created_at', 'is_global']

class CoursePostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    course = CourseSerializer()

    class Meta:
        model = CoursePost
        fields = ['id', 'user', 'course', 'content', 'created_at', 'is_global']
