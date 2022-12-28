from dataclasses import field
from api.models import Student

from rest_framework.serializers import ModelSerializer
class StudentSerializer(ModelSerializer):
    class Meta:
        model=Student
        fields=['name']