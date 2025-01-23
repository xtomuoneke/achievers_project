"""
URL configuration for achievers_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from achievers_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/achievers_app/', include('achievers_app.urls')),
    path('user_manager_app/', include('user_manager_app.urls')),
    # path('user_manager_app/', include('user_manager_app.urls')),
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

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
