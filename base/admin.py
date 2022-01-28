from django.contrib import admin
from .models import Comment, Post, Category, userProfile
# Register your models here.
# admin.site.register(model_name) #If not there, then its not visible in admin area
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(userProfile)
admin.site.register(Comment)
