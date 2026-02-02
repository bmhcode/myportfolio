from django.shortcuts import render, redirect
from .models import About, Skill, Project, Service
from .forms import ProjectForm

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

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'core/add_project.html', {'form': form})
