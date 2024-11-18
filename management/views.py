from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.http import JsonResponse 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, logout as singout 
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import *



def home(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'management/home.html', {'profile': profile})


@login_required(login_url="/management/login")
def management(request):
    return render(request,'management.html')

@login_required(login_url="/management/login")
def home (request):
    return render(request,'management/home.html')

# @login_required(login_url="/account/login")
def profile(request):

    
    context = {
         "all_profile" : User,

        }

    return render(request,'management/profile.html',context,)    

#@login_required(login_url="/account/login")
def login(request):
    message = None
    if request.method == 'POST':   
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user) 
                return redirect('management:home')
            else:
                message = "Invalid credentials"
        else:
            message = "Username and Password are required"
    
    context = {
        "message": message
    }

    return render(request,'management/login.html', context)

def signup(request): 
    massage = None 
    if request.method == 'POST': 
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
 
        if username and email and password: 
            user = User.objects.create_user( 
                username=username, 
                email=email,
                password=password ,
            ) 
            user.save() 
            login(request, user)
            return redirect('management:home') 
        else: 
            massage = "username and password is requard" 
 
    context = { 
        'massage' : massage 
    } 
 
    return render(request, 'management/signup.html', context) 

def logout(request): 
    singout(request) 
    return redirect('management:login')






def my_taim(request):

    return render (request,'management/my_taim.html')

@login_required



def profile_edit(request, id):
    try:
        profile = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        raise Http404(f"Profile does not exist with id: {id}")

    if request.method == 'POST':
        fathers_name = request.POST.get('fathers_name')
        mothers_name = request.POST.get('mothers_name')
        profile_image = request.FILES.get('profile_image')  # Use request.FILES for file uploads
        address = request.POST.get('address')
        blood_group = request.POST.get('blood_group')
        email = request.POST.get('email')

        
        profile.fathers_name = fathers_name
        profile.mothers_name = mothers_name
        profile.profile_image = profile_image
        profile.address = address
        profile.blood_group = blood_group
        profile.email = email

       
        profile.save()
        messages.success(request, 'Your profile has been successfully updated!')                       
        return redirect("management:profile")
    context = {
        'profile': profile,
    }

    return render(request, 'management/profile_edit.html', context)


def superuser_info(request):
    if not request.user.is_authenticated:  
        return redirect('login')
    if not request.user.is_superuser:  
        return redirect('home')  
    superusers = User.objects.filter(is_superuser=True)
    context = {
        'superusers': superusers,
        'superuser_count': superusers.count(),
    }
    return render(request, 'management/superuser_info.html', context)