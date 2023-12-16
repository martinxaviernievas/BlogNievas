from django.contrib import admin
from .models import Post




class PostAdmin(admin.ModelAdmin):
    fields = ('title','slug','created_on','content')

    prepopulated_fields = {'slug': ('title',)}