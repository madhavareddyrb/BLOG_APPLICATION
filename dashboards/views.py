from django.shortcuts import redirect, render
from blog_app.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
  category_count = Category.objects.all().count()
  blog_count = Blog.objects.all().count()
  context = {
    'category_count': category_count,
    'blog_count': blog_count,
  }
  return render(request, 'dashboard/dashboard.html', context)

def categories(request):
  return render(request, 'dashboard/categories.html')

def add_category(request):
  if request.method == "POST":
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('categories')

  form = CategoryForm()
  context = {
    'form': form,
    
  }
  return render(request, 'dashboard/add_category.html', context)

def edit_category(request):
  
