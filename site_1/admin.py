from django.contrib import admin

# Register your models here.
from .models import Project, Building

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'created_at']
    search_fields = ['name', 'city']

class BuildingInline(admin.TabularInline):
    model = Building
    extra = 1

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'floors', 'apartments_count', 'status']
    list_filter = ['project', 'status']