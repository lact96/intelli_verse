# academies/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AcademyViewSet, ProfessorViewSet, AcademyProfessorViewSet

router = DefaultRouter()
router.register(r'academies', AcademyViewSet)
router.register(r'professors', ProfessorViewSet)
router.register(r'academy-professors', AcademyProfessorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
