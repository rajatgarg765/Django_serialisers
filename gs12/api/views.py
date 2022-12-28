from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from rest_framework.views import APIView

from api.models import Student
from api.serializers import StudentSerializer

class StudentView(APIView):
    def get(self,request):
        stu=Student.objects.all()
        print(stu)
        s=StudentSerializer(stu,many=True)
        print(s)
        return Response(s.data)