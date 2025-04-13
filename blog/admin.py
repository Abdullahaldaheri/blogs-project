from django.contrib import admin
from .models import User, Post, Comment, Category  # Use CustomUser if you renamed it

# Register your models here
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
