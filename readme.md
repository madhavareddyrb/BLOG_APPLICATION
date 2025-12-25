## BLOG APPLICATION:

create folder:

uv pip install django

django-admin startproject blog_main

to create super user we first run migrate command

py manage.py migrate

py manage.py createsuperuser

chnage default page to home page 

path(' ' , views.home, name = 'home")

create views.py file

create a function home
### Basic View function (view Function always take request)

def home(request)

return HttpResponse("h2>HOe age<?H2>)

change to render home.html

create templtaes folde and teitle django blogg settings configue templates
design home page:

bootstrap--select blog layouy

## Static files Configuration:

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR /'static'
STATICFILES_DIRS = [
  'blog_main/static',
]


in templates {% load static %}

link css using template tag (process) {% static 'css/blog.css' %}


