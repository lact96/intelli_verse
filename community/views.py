from django.shortcuts import render

# Create your views here.
# community/views.py

from rest_framework import viewsets
from .models import CommunityPost, CoursePost
from .serializers import CommunityPostSerializer, CoursePostSerializer

class CommunityPostViewSet(viewsets.ModelViewSet):
    queryset = CommunityPost.objects.all()
    serializer_class = CommunityPostSerializer

class CoursePostViewSet(viewsets.ModelViewSet):
    queryset = CoursePost.objects.all()
    serializer_class = CoursePostSerializer
