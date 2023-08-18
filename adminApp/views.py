from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.generic import TemplateView
from .models import Teacher


# Create your views here.
def adminHomeView(request):
    return render(request, 'admin1/base.html')

class addTeacher(TemplateView):
    template_name = 'admin2/addTeacher.html'
    permission_classes = [AllowAny]
    def post(self, request):
        teacherName =request.POST.get('teacherName')
        department = request.POST.get('department')
        email = request.POST.get('email')
        phone =  request.POST.get('phone')
        gender = request.POST.get('gender')
        address =  request.POST.get('address')
        profile_pic = request.POST.get('profile_pic')
        password = request.POST.get('password')
        print(teacherName, department, email,profile_pic)
        checkTeacher = Teacher.objects.filter(email = email).first()
        if not checkTeacher:
            getTeacher = Teacher.objects.create(
                teacherName = teacherName, department_id = int(department), phone = phone, email = email,
                gender = gender, address = address, profile_pic = profile_pic, password = password

            )
            if getTeacher:
                messages.add_message(request, messages.INFO, 'Teacher Added Successfully ')  
                return redirect( '/adminApp/addTeacher/')
            else:
                messages.add_message(request, messages.INFO, 'Something Went Wrong')  
                return redirect( '/adminApp/addTeacher/')



        else:
            messages.add_message(request, messages.INFO, 'Teacher Addition Failed') 
            return redirect( '/adminApp/addTeacher/')
        
# class manageTeacher(TemplateView):
#     template_name = 'manageTeacher.html'
#     # permission_classes = [AllowAny]
#     def get(self, request):
#         print("Hello world")
#         return redirect( '/adminApp/manageTeacher/')
def manageTeacher(request):
    if request.method =="GET":
        alldata = Teacher.objects.all()
    
    return render(request, 'admin1/manageTeacher.html', {'teacherInfo': alldata})

def updateData(request, id):
    item = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        # Retrieve updated data from POST request
        teacherName =request.POST.get('teacherName')
        department = request.POST.get('department') 
        designamtion = request.POST.get('designamtion') 
        print("hello", department)
        email = request.POST.get('email')
        phone =  request.POST.get('phone')
        gender = request.POST.get('gender')
        address =  request.POST.get('address')
        profile_pic = request.POST.get('profile_pic')
        password = request.POST.get('password')

        
        # new_name = request.POST['new_name']
        # Update the item's data
        item.teacherName = teacherName
        item.department_id = int(department)
        item.designamtion = designamtion
        item.email = email
        item.phone = phone
        item.gender = gender
        item.address = address
        item.profile_pic = profile_pic
        item.password = password

        item.save()
        return redirect('/adminApp/manageTeacher/', id=id)  # Redirect to detail page
    return render(request, 'admin1/update.html', {'item': item})

    


def deleteData(request, id):
    item = get_object_or_404(Teacher, id=id)
    if request.method=="POST":
        item.delete()
        return redirect('/adminApp/manageTeacher/')
        
    return render(request, 'admin1/delete.html', {'item': item})
