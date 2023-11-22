"""
URL configuration for HealthControll project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index),
    path("", views.index),
    path("index/record/", views.record),
    path('accounts/', include('UserModel.urls')),
    path("index/make_fit_plan/", views.make_fit_plan),
    path("index/make_diet_plan/", views.make_diet_plan),
    path("index/make_part_plan/", views.make_part_plan),
]
