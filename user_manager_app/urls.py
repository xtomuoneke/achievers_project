from django.contrib import admin
from django.urls import path
from user_manager_app import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Register

# Please, put all the urls specific to user_manager_app here
path('Register', Register, name='register'),