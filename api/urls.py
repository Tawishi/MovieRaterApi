from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import router

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
