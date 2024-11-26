from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('addition/', views.addition, name='addition'),  # Addition page
    path('subtraction/', views.subtraction, name='subtraction'),  # Subtraction page
    path('multiplication/', views.multiplication, name='multiplication'),  # Multiplication page
    path('division/', views.division, name='division'),  # Division page
]
