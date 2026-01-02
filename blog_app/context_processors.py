from .models import *
from assignments.models import Social_Media

def get_categories(request):
  categories = Category.objects.all()
  return dict(categories = categories)

def get_social_media(request):
  social_media = Social_Media.objects.all()
  return dict(social_media = social_media)
