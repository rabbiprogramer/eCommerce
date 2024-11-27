from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.http import JsonResponse 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, logout as singout 
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomSuperuserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ProductForm
from.forms import ProfileForm
from .models import *


@login_required(login_url='/management/login')
def home(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'management/home.html', {'profile': profile})

def add_new(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    if not request.user.is_superuser:
        return redirect('management:home') 
    if request.method == 'POST':
        form = CustomSuperuserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Superuser created successfully!")
            return redirect('management:home')
        else:
            print(form.errors)  # Log the form errors
            messages.error(request, "Form submission failed. Please check the fields.") 
    else:
        form = CustomSuperuserForm() 

    return render(request, 'management/add_new.html', {'form': form})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_product') 
        else:
            print(form.errors)  
    else:
        form = ProductForm()
        print(request.POST)
        print(request.method)
        
    return render(request, 'management/add_product.html', {'form': form})


def all_product(request):
    products = Product.objects.all()
    return render(request, 'management/all_product.html', {'products': products})


@login_required(login_url="/management/login")
def management(request):
    return render(request,'management.html')

@login_required(login_url="/management/login")
def home (request):
    return render(request,'management/home.html')

# @login_required(login_url="/management/login")
def profile(request):
    try:
        # Try to get the profile of the logged-in user
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        # If the request method is POST, instantiate the form with the posted data and files
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Save the updated profile
            return redirect('management:profile')  # Redirect to the same profile page after successful save
    else:
        # If the request method is GET, just instantiate the form with the profile data (if it exists)
        form = ProfileForm(instance=profile)

    # Make sure 'form' is always passed to the context
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'management/profile.html', context)


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

    return render(request, 'management/login.html', {"message": message})

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
        return redirect('management:login')  

    if not request.user.is_superuser:
        return redirect('management:home')  
   
    superusers = User.objects.filter(is_superuser=True)
    
    if superusers.count() == 0:
        return redirect('management:login') 
    context = {
        'superusers': superusers,
        'superuser_count': superusers.count(),
    }
    
    # Render the superuser_info page
    return render(request, 'management/superuser_info.html', context)



def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('management:all_product') # Redirect to product list after editing
    else:
        form = ProductForm(instance=product)
    return render(request, 'management/product_edit.html', {'form': form})

def product_delete(request, id):

    product = get_object_or_404(Product, id=id)
    
   
    product.delete()
    

    return redirect('management:all_product')

def superuser_delete(request, id):
    if request.method == 'POST':
        superuser_info = get_object_or_404(User, id=id, is_superuser=True)
        superuser_info.delete()
        messages.success(request, "Superuser deleted successfully.")
    else:
        messages.error(request, "Invalid request.")
    return redirect('management:superuser_info')




def card (request):
    return render(request,'management/card.html')