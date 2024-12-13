from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('Math/', views.Math, name='Math'),  # Math page
]
