from django.shortcuts import render,  HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import hashlib, json
from .models import EndUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.generic import TemplateView

def get_tokens_for_user(get_user): 
    refresh = RefreshToken.for_user(get_user)
    return  str(refresh.access_token)

    # return {
    #     'refresh': str(refresh),
    #     'access': str(refresh.access_token),
    # }


# Create your views here.
def home1View(request):
    return render(request, 'student/index.html')

def homeView(request):
    return render(request, 'admin2/base.html')

def registrationView1(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        city = request.POST.get('city')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        if password == confirmPassword:
            print(firstName, lastName,email,country,phone,city,password)
            hashPassword = hashlib.md5(password.encode('utf-8')).hexdigest()
            getUser = EndUser.objects.create(
                firstName=firstName, lastName=lastName,
                email = email, phone=phone, country=country,
                city = city, password = hashPassword)
            if getUser:
                token = get_tokens_for_user(getUser)
                jsonData = {}
                jsonData['id'] = getUser.id 
                jsonData['firstName'] = getUser.firstName
                jsonData['lastName'] = getUser.lastName
                jsonData['email'] = getUser.email
                jsonData['phone'] = getUser.phone
                jsonData['country'] = getUser.country

                print("registration successful")

                return Response({'message':'registration successfull','token': token, 'results':jsonData}, status= status.HTTP_201_CREATED)
            
        else:
            print("password and confirm password does not match")

    return render(request, 'student/registration.html')

class registrationView(TemplateView):
    template_name = 'student/registration.html'
    permission_classes = [AllowAny]
    def post(self, request,*args, **kwargs):
        firstName =request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        phone =  request.POST.get('phone')
        country = request.POST.get('country')
        city =  request.POST.get('city')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        # confirmPassword = '2'

        if password == confirmPassword:
            print(firstName, lastName,email,country,phone,city,password)
            hashPassword = hashlib.md5(password.encode('utf-8')).hexdigest()
            checkUser = EndUser.objects.filter(email = email, phone = phone)
            if not checkUser:
                getUser = EndUser.objects.create(
                    firstName=firstName, lastName=lastName,
                    email = email, phone=phone, country=country,
                    city = city, password = hashPassword)
                if getUser:
                    token = get_tokens_for_user(getUser)
                    jsonData = {}
                    jsonData['id'] = getUser.id 
                    jsonData['firstName'] = getUser.firstName
                    jsonData['lastName'] = getUser.lastName
                    jsonData['email'] = getUser.email
                    jsonData['phone'] = getUser.phone
                    jsonData['country'] = getUser.country

                    print("registration successful")

                    # return Response({'message':'registration successfull','token': token, 'results':jsonData}, status= status.HTTP_201_CREATED)
                    return render(request, 'student/login.html')
            
        else:
            messages.add_message(request, messages.INFO, 'Wrong Password')
            return redirect('/registration/')
            


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