from django.contrib import admin
from django.urls import path

from UserModel import views

urlpatterns = [
    path("", views.login),
    path("login/", views.login),
    path("register/", views.register),
    path("logout/", views.logout),
]
