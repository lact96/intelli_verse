# community/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommunityPostViewSet, CoursePostViewSet

router = DefaultRouter()
router.register(r'community-posts', CommunityPostViewSet)
router.register(r'course-posts', CoursePostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
