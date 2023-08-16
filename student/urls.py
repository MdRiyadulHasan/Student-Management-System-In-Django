from django.urls import path, include
from . import views

urlpatterns = [
    # path('home/', views.homeView),
    path('home/', views.homeView),
    path('home1/', views.home1View),
    path('login/', views.loginPageView.as_view(), name = "login"),
    path('registration/', views.registrationView.as_view(), name = "registration"),
    # path('registration/', views.registrationView1, name = "registration"),
    path('doLogin', views.doLogin),
]
