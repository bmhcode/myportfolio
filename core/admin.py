from django.contrib import admin
from .models import About, Skill, Service, Project

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email')
    
    def has_add_permission(self, request):
        # Allow only one instance if one exists
        if About.objects.exists():
            return False
        return True

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'links_display')
    
    def links_display(self, obj):
        return obj.link
    links_display.short_description = 'Link'
