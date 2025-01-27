from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Please, put all the urls specific to user_manager_app here
from django.urls import path


urlpatterns = [
    path('instructor/dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
