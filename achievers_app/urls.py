from django.contrib import admin
from django.urls import path
from achievers_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about-us/', views.about_us, name='about-us'),
    path('course-secondary/', views.about_us, name='course-secondary'),
    path('our-values/', views.our_values, name='our-values'),
    path('gallery/', views.gallery, name='gallery'),
    path('other-course/', views.other_course, name='other-course'),
    path('higher-secondary/', views.higher_secondary, name='higher-secondary'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('our-team/', views.our_team, name='our-team'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
