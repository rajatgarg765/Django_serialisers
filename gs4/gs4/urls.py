
from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api),
    path('studentapi/<int:pk>', views.student_api),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),

]
