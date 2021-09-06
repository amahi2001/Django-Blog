from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.

def allblogs(request):
    blogs = Blog.objects

    #will; contain all the variables we pass in
    context = {'blogs':blogs}

    return render(request, 'blog/allblogs.html', context)

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {"blog":detailblog})
