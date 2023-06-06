from django.contrib import admin
from .models import (
    About_me,
    Skills,
    Education,
    Experience,
    Projects,
)

admin.site.site_header = 'My Portfolio Admin Panel'
admin.site.site_title = 'My Portfolio Admin Panel'
admin.site.index_title = 'My Portfolio Admin Panel'

@admin.register(About_me)
class About_meAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'age', 'email', 'phone', 'address', 'github', 'linkedin', 'facebook', 'instagram', 'telegram', 'photo', 'description']
    fields = ['name', 'surname', 'age', 'email', 'phone', 'address', 'github', 'linkedin', 'facebook', 'instagram', 'telegram', 'photo', 'description']
    # exclude = ['name', 'surname', 'age', 'email', 'phone', 'address', 'github', 'linkedin', 'facebook', 'instagram', 'telegram', 'photo', 'description']

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'skill_icon', 'skill_description', 'skill_document']
    fields = ['skill_name', 'skill_icon', 'skill_description', 'skill_document']
    # exclude = ['skill_name', 'skill_icon', 'skill_description', 'skill_document']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['education_name', 'education_icon', 'education_description', 'education_link']
    fields = ['education_name', 'education_icon', 'education_description', 'education_link']
    # exclude = ['education_name', 'education_icon', 'education_description']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['experience_name', 'experience_description', 'experience_link']
    fields = ['experience_name', 'experience_description', 'experience_link']

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_description', 'project_image', 'project_link', 'project_github', 'about_me']
    fields = ['project_name', 'project_description', 'project_image', 'project_link', 'project_github', 'about_me']
    # exclude = ['project_name', 'project_description', 'project_image', 'project_link', 'project_github', 'about_me']
