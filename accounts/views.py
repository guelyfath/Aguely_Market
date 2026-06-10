from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request,'login.html')

def password_reset_view(request):
    return render(request,'password_reset.html')

def profile_view(request):
    return render(request,'profile.html')

def register_view(request):
    return render(request,'register.html')