from django.contrib import admin
from .models import Academy, Professor, AcademyProfessor

admin.site.register(Academy)
admin.site.register(Professor)
admin.site.register(AcademyProfessor)