# videos/serializers.py

from rest_framework import serializers
from .models import VideoPost
from users.serializers import CustomUserSerializer

class VideoPostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = VideoPost
        fields = ['id', 'user', 'video', 'title', 'description', 'created_at', 'is_academy_post']
