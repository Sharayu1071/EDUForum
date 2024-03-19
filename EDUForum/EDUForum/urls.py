"""Task1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static
from django.views.static import serve
from Admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lg/',views.login_page,name= "loginpage"),
    path('rg/',views.register, name= "registrationpage"),
    path('ad/',views.ask_doubt,name="askdoubt"),
    path('', views.home, name="home"),
    path('home/', views.home1, name="home1"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('placement/',views.placement,name="placement"),
    path('insights/', views.insights, name="insights"),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT}),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)