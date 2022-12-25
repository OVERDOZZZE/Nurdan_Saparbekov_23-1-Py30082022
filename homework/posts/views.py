from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Product

# Create your views here.


def main_view(request):
    return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method =='GET':
        posts = Product.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Product.objects.get(id=id)
        context = {
            'post': post,
            'reviews': post.reviews.all()
        }
        return render(request, 'posts/detail.html', context=context)
