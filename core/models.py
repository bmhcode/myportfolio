from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    experience_years = models.IntegerField(default=15)
    
    # Contact info
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, blank=True)
    github = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "About Me"

    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('tools', 'Tools & Deployment'),
    )
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class (e.g., bi-code-slash)")

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200, help_text="Comma separated technologies")
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title
