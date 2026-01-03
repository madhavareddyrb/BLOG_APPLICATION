from django.shortcuts import render,redirect
from blog_app.models import *
from assignments.models import *
from .forms import RegistrationForm
def home(request):
  
  #featured_posts = Blog.objects.filter(is_featured = True, status = "Published").order_by("updated_at")
  featured_post = Blog.objects.filter(is_featured = True,status='published')
  featured_posts = Blog.objects.filter(is_featured = True, status = 'published')
  posts = Blog.objects.filter(is_featured = False, status= 'published')
  try:
    about = About.objects.get()
  except:
    about = "none"

  context = {
    'featured_post': featured_post,
    'featured_posts': featured_posts,
    'posts': posts,
    'about': about,
  }

  return render(request, "home.html", context)


def register(request):
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("register")
  else:
    form = RegistrationForm()
  context = {
    'form': form,
  }
  return render(request, 'register.html', context)
