from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from .models import Project

def home(request):
    context = {
        'name': 'srujith sharma',
        'myphoto': '/Users/srujit/Desktop/img.jpg',
        'email': 'srujit2198@email.com',
        'worktitle': 'Freelance Web Developer',
        'mydescription': 'I am a skilled web developer with experience in Django and Python.',
        'phonenumber': '2013449602'
    }
    return render(request, 'home.html', context)

def portfolio(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio.html', context)

def about(request):
    return render(request, 'about.html')
