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
  category = get_object_or_404(Category, pk=category_id)
  context = {
    'blog_category' : blog_category,
    'category' : category,
  }

  return render(request, 'posts_by_category.html', context)