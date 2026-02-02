from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'link', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Project Description'}),
            'technologies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Technologies Used'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Project Link'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
