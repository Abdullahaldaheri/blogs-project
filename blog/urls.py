from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('landing/main/', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('blog/', views.blogs, name='blog'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('blog/<int:post_id>/', views.blog_details, name='blog_details'),
]
