from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('addition/', views.addition, name='addition'),  # Addition page
]
