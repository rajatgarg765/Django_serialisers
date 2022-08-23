from wsgiref.validate import validator
from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validate_data):
        print(instance.name)
        instance.name=validate_data.get("name",instance.name)
        print(instance.name)
        instance.roll=validate_data.get("roll",instance.roll)
        instance.city=validate_data.get("city",instance.city)
        instance.save()
        return instance
        
    #field level validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat Full")
        return value