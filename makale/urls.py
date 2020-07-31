from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.blogView, name="blog"),
    path('makale/<int:id>',views.detail, name= "detail"),
]