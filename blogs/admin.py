# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Post


admin.site.register(Blog)
admin.site.register(Post)