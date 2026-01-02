from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q

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

def search(request):
  keyword = request.GET.get('keyword')
  print(keyword)
  #blogs = Blog.objects.filter(title__icontains = keyword , status = "published")
  blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body__icontains = keyword), status = "published")
  print(blogs)
  
  context = {
    'blogs': blogs,
    'keyword': keyword,
  }
  return render(request, 'search.html', context)