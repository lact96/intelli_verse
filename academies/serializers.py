# academies/serializers.py

from rest_framework import serializers
from .models import Academy, Professor, AcademyProfessor
from users.serializers import UserProfileSerializer

class AcademySerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer()
    professors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Academy
        fields = ['id', 'owner', 'name', 'description', 'approved', 'professors']

class ProfessorSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    academies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Professor
        fields = ['id', 'user', 'academies']

class AcademyProfessorSerializer(serializers.ModelSerializer):
    academy = AcademySerializer()
    professor = ProfessorSerializer()

    class Meta:
        model = AcademyProfessor
        fields = ['id', 'academy', 'professor', 'permissions']
