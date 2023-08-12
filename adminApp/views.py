from django.shortcuts import render

# Create your views here.
def adminHomeView(request):
    return render(request, 'admin1/base.html')
