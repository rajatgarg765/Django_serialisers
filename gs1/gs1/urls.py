"""gs1 URL Configuration

"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>',views.student_detail),
    path('stuinfo/',views.student_list),
    path('stucreate/',views.student_create),
    path('studentapi/',views.student_api),
    #path('studentapi/',views.StudentAPI.as_view()),
]
