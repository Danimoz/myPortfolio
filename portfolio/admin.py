from django.contrib import admin
from .models import Blog, Skill, Project, Newsletter
# Register your models here.
admin.site.register(Blog)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Newsletter)
