
from django.contrib import admin
from django.urls import path,include

from api.views import StudentList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', StudentList.as_view()),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
]
