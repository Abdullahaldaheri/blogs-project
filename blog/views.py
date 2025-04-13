
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(request, 'blog/landing.html')


def main(request):
    template = loader.get_template('main.html')
    return render(request, 'blog/main.html')

def users(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {'users': users})

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})

def blog_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/blogdetails.html', {'post': post})
