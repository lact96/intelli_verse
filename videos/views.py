# videos/views.py

from rest_framework import viewsets
from .models import VideoPost
from .serializers import VideoPostSerializer

class VideoPostViewSet(viewsets.ModelViewSet):
    queryset = VideoPost.objects.all()
    serializer_class = VideoPostSerializer
