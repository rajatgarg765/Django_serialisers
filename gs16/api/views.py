from django.shortcuts import render

# Create your views here.
from .serializers import StudentSerializer

from .models import Student

from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    # queryset=Student.objects.filter(passby="user1")
    serializer_class=StudentSerializer
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)