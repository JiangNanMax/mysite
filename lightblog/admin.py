from django.contrib import admin
from .models import LightBlog

# Register your models here.
@admin.register(LightBlog)
class LightBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_time')