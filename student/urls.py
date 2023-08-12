from django.urls import path, include
from . import views

urlpatterns = [
    # path('home/', views.homeView),
    path('home/', views.homeView),
    path('addStaff/', views.addStaff, name = "addStaff"),
    path('home1/', views.home1View),
    path('', views.loginPage),
    path('registration/', views.registrationView, name = "registration"),
    path('doLogin', views.doLogin),
]
