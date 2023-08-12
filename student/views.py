from django.shortcuts import render,  HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password


# Create your views here.
def home1View(request):
    return render(request, 'student/index.html')

def homeView(request):
    return render(request, 'admin2/base.html')

def registrationView(request):
    return render(request, 'student/registration.html')

def loginPage(request):
    return render(request, 'student/login.html')

def addStaff(request):
    return render(request, 'admin2/add_staff.html')

def doLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        hashed_password = make_password(password1, salt='cehfqdttWMqelxsQkJ4dRv')
        if hashed_password == request.user.password:

            return HttpResponseRedirect("home/")
        else:

            return HttpResponse('Error Login ')