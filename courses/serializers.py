# courses/serializers.py

from rest_framework import serializers
from .models import Course, Enrollment, Subscription
from academies.serializers import AcademySerializer
from users.serializers import CustomUserSerializer

class CourseSerializer(serializers.ModelSerializer):
    academy = AcademySerializer()

    class Meta:
        model = Course
        fields = ['id', 'academy', 'title', 'description', 'price', 'is_free', 'is_subscription_based', 'content']

class EnrollmentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'progress']

class SubscriptionSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    academy = AcademySerializer()

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'academy', 'start_date', 'end_date']
