from django.urls import path, include
from . import views

urlpatterns = [
    path('abc/', views.homeView),
]
