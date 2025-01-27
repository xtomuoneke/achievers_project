from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.home, name='home'), 
    path('logout/', views.logout_view, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('AboutCoachingC/', views.AboutCoachingC, name='AboutCoachingC'),
    path('our_values/', views.AboutCoachingC, name='our_values'),
    path('our_team/', views.our_team, name='our_team'),
    path('course_secoundary/', views.our_team, name='course_secoundary'),
    path('higher_secoundary/', views.our_team, name='higher_secoundary'),
    path('othercourse/', views.our_team, name='othercourse'),
    path('gallery/', views.gallery, name='gallery'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('contact_us/', views.contact_us, name='contact_us'),




]