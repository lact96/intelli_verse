# videos/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoPostViewSet

router = DefaultRouter()
router.register(r'video-posts', VideoPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
