# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project

def home(request):
    context = {
        'name': 'Srujith Sharma',
        'myphoto': '/static/photo.jpg',
        'email': 'srujit2198@gmail.com',
        'linkedin': 'Srujith Sharma',
        'worktitle': 'Freelance Web Developer',
        'mydescription': 'I am a skilled web developer with 3 years of experience in Django and Python. My journey in web development has been marked by a passion for crafting robust and scalable solutions that push the boundaries of what\'s possible. With a strong foundation in Django and Python, I have honed my skills in creating dynamic and feature-rich web applications that meet the diverse needs of clients and users alike.',
        'phonenumber': '2013449602'
    }
    return render(request, 'home.html', context)

@login_required
def portfolio(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio.html', context)

def about(request):
    return render(request, 'about.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portfolio')  # Redirect to portfolio page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout
