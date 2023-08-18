from django.urls import path
from . import views

urlpatterns = [
    path('adminhome/', views.adminHomeView),
    path('addTeacher/', views.addTeacher.as_view(), name = "addTeacher"),
    path('manageTeacher/', views.manageTeacher, name = "manageTeacher"),
    path('updateData/<int:id>/', views.updateData, name = "deleteData"),
    path('deleteData/<int:id>/', views.deleteData, name = "deleteData"),
 
]