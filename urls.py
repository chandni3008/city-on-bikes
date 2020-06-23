from django.contrib import admin
from django.urls import path
from .views import register,login,index
urlpatterns = [
    path('', index, name='index'),
]