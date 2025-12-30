from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.
def blogs_by_category(request, category_id):
  blog_category = Blog.objects.filter(status= 'published', category = category_id)
  #try:
    #category = Category.objects.get(pk=category_id,status='published')
  #except:
    #return redirect('home')
  context = {
    'blog_category' : blog_category,
  }

  return render(request, 'posts_by_category.html', context)


def single_bolg(request, slug):
  single_blog = get_object_or_404(Blog, slug = slug, status="published")
  context = {
    'single_blog': single_blog,
  }
  return render(request, 'single_blog.html', context)