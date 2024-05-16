# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, ProfessorProfileViewSet, CourseViewSet, LessonViewSet, VideoViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'professor-profiles', ProfessorProfileViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
