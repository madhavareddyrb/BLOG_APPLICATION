from django.shortcuts import render
from blog_app.models import *
def home(request):
  
  #featured_posts = Blog.objects.filter(is_featured = True, status = "Published").order_by("updated_at")
  featured_post = Blog.objects.filter(is_featured = True,status='published')
  featured_posts = Blog.objects.filter(is_featured = True, status = 'published')
  posts = Blog.objects.filter(is_featured = False, status= 'published')
  context = {
    'featured_post': featured_post,
    'featured_posts': featured_posts,
    'posts': posts,
  }

  return render(request, "home.html", context)