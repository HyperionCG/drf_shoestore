from django.urls import path
from shoeapp import views

urlpatterns = [
    path('', views.index, name = 'home')
    ]