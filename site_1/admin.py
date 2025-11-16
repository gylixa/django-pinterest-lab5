# site_1/admin.py

from django.contrib import admin
from .models import Project, Building, Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'supplier']
    list_filter = ['type']
    search_fields = ['name', 'supplier']


class BuildingInline(admin.TabularInline):
    model = Building
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'created_at']
    search_fields = ['name', 'city']
    inlines = [BuildingInline]

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'floors', 'apartments_count', 'status']
    list_filter = ['project', 'status', 'materials']
    filter_horizontal = ('materials',)  # ← удобный выбор материалов!