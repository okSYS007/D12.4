from django.contrib import admin
from .models import Category, Post

class ProductAdmin(admin.ModelAdmin):
    list_display = ('post_author', 'post_title', 'post_text', 'post_rate') 
    list_filter = ('post_author', 'post_rate') 
    search_fields = ('post_title', 'post_text') 

admin.site.register(Category)
admin.site.register(Post, ProductAdmin)