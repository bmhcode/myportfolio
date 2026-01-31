from django.shortcuts import render
from .models import About, Skill, Project, Service

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    
    context = {
        'about': about,
        'skills': skills,
        'projects': projects,
        'services': services,
    }
    return render(request, 'home.html', context)
