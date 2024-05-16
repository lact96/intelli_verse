# views.py
from rest_framework import viewsets
from .models import UserProfile, ProfessorProfile, Course, Lesson, Video, Subscription
from .serializers import UserProfileSerializer, ProfessorProfileSerializer, CourseSerializer, LessonSerializer, VideoSerializer, SubscriptionSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ProfessorProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfessorProfile.objects.all()
    serializer_class = ProfessorProfileSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
