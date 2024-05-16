from django.shortcuts import render

# Create your views here.
# academies/views.py

from rest_framework import viewsets
from .models import Academy, Professor, AcademyProfessor
from .serializers import AcademySerializer, ProfessorSerializer, AcademyProfessorSerializer

class AcademyViewSet(viewsets.ModelViewSet):
    queryset = Academy.objects.all()
    serializer_class = AcademySerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class AcademyProfessorViewSet(viewsets.ModelViewSet):
    queryset = AcademyProfessor.objects.all()
    serializer_class = AcademyProfessorSerializer
