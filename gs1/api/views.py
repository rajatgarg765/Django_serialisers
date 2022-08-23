from http.client import HTTPResponse
import io
import json
from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
# Create your views here.

#model object -single student data

#function based view

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    #print(stu)
    serializer=StudentSerializer(stu)
    #print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data,content_type="application/json")

# query set all student data
def student_list(request):
    stu=Student.objects.all()
    #print(stu)
    serializer=StudentSerializer(stu,many=True)
    #print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data,content_type="application/json")
    #we can also do 
    #return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def student_create(request):
    if request.method=="POST":
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        print(stream)
        python_data=JSONParser().parse(stream)
        print(python_data)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data inserted"}
            j_data=JSONRenderer().render(res)
            return HttpResponse(j_data,content_type="application/json")

        js_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(js_data,content_type="application/json")
        
@csrf_exempt
def student_api(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get("id",None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return JsonResponse(serializer.data,safe=False)
        
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data Inserted"}
            return JsonResponse(res)

        js_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(js_data,content_type="application/json")

    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get("id")
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data Updated"}
            return JsonResponse(res)

        js_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(js_data,content_type="application/json")

    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get("id")
        stu=Student.objects.get(id=id)
        stu.delete()
        res={"msg":"Data Deleted"}
        return JsonResponse(res)


# from django.utils.decorators import method_decorator
# from django.views import View

# @method_decorator(csrf_exempt,name="dispatch")
# class StudentAPI(View):
#     def get(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get("id",None)
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return JsonResponse(serializer.data,safe=False)
        
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return JsonResponse(serializer.data,safe=False)
    
#     def post(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res={"msg":"Data Inserted"}
#             return JsonResponse(res)

#         js_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(js_data,content_type="application/json")

#     def put(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get("id")
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={"msg":"Data Updated"}
#             return JsonResponse(res)

#         js_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(js_data,content_type="application/json")

#     def delete(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get("id")
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         res={"msg":"Data Deleted"}
#         return JsonResponse(res)




