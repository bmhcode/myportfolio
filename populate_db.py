import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from core.models import About, Skill, Project, Service

def populate():
    # About
    if not About.objects.exists():
        About.objects.create(
            name="Mohamed",
            role="Développeur Backend Django",
            bio="Développeur web avec plus de 15 ans d’expérience en programmation, spécialisé dans la création d’applications web avec Python et Django. Je conçois des solutions pratiques, faciles à maintenir et orientées métier, en accord avec les besoins réels des clients.",
            experience_years=15,
            email="contact@mohamed.dev",
            whatsapp="1234567890",
            github="https://github.com/mohamed"
        )
        print("Created About section")

    # Skills
    skills_data = [
        ('Python', 'backend'), # Corrected category case to match tuple
        ('Django', 'backend'),
        ('Django REST Framework', 'backend'),
        ('PostgreSQL', 'backend'),
        ('HTML / CSS', 'frontend'),
        ('Bootstrap', 'frontend'),
        ('Git / GitHub', 'tools'),
        ('Docker', 'tools'),
        ('VPS / Railway', 'tools'),
    ]
    
    for name, cat in skills_data:
        Skill.objects.get_or_create(name=name, category=cat)
    print(f"Created {len(skills_data)} skills")

    # Services
    services_data = [
        ('Développement Web', 'Création d’applications web complètes, robustes et sécurisées avec Django.', 'bi-code-slash'),
        ('Systèmes de Gestion (CRUD)', 'Conception d\'outils internes et tableaux de bord sur mesure.', 'bi-database'),
        ('API & Déploiement', 'Création d\'API REST et mise en production sur serveurs VPS ou Cloud.', 'bi-hdd-network'),
    ]

    for title, desc, icon in services_data:
        Service.objects.get_or_create(title=title, description=desc, icon=icon)
    print(f"Created {len(services_data)} services")

    # Projects
    projects_data = [
        {
            'title': 'Khidma',
            'description': 'Plateforme web permettant aux professionnels et prestataires de services de s’inscrire afin de faciliter la recherche de services par catégorie et localisation.',
            'technologies': 'Django, PostgreSQL',
            'link': 'https://khidma.com'
        },
        {
            'title': 'Système de Gestion CRUD',
            'description': 'Application de gestion complète avec authentification, permissions avancées et rapports dynamiques.',
            'technologies': 'Django, Bootstrap',
            'link': 'https://example.com'
        }
    ]

    for proj in projects_data:
        Project.objects.get_or_create(
            title=proj['title'],
            defaults={
                'description': proj['description'],
                'technologies': proj['technologies'],
                'link': proj['link']
            }
        )
    print(f"Created {len(projects_data)} projects")

if __name__ == '__main__':
    populate()
