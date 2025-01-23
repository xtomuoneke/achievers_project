from django.contrib import admin
from django.urls import path
from user_manager_app import views
from django.conf import settings
from django.conf.urls.static import static

# Please, put all the urls specific to user_manager_app here

urlpatterns = [
    path('registration_page/', views.registration_page, name='registration_page'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)