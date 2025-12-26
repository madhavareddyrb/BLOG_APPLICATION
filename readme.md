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


## Use GITIGNORE.Io
create .gitignore file and add all the things that give from gitignore.io 

### Category Model (different types of blog)

To Manage all blogs create a app using py manage.py startapp blogs and configure name in settings

Create A Model for category:

class Category(models.Model):
  category_name = models.CharField(max_length = 50, unique = True), createdat and Updated at

Make Migrations : py manage.py makemigrations

Migrate: py manage.py migrate

Register that model in admin-- admin.site.register(catagory) and import model

django adds plural automatically to avoid it we use verbose -- in model 

in model --> class Meta:
          verbose_name_plural = 'category'

          def __str__(self):
            return self.category_name


### Media Files Configuration:
Media files = user-uploaded files.



create folder in root level. settings.py --> MEDIA_URL = '/media/'
            MEDIA_ROOT = BASE_DIR /'media'

MEDIA_ROOT= This is the folder in your project where uploaded files get stored from user 
MEDIA_URL = This is the URL prefix used to access those files in the browser(ex: when we click on image and open in new tab.)           

in urls.py -> ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls.static import static

from django.conf import settings

Very Important Note

🔴 Django does NOT serve media files in production.

In real deployments:

Nginx / Apache or cloud storage (S3, etc.) serves them

Because Django is not optimized for file serving

The static() helper is only for development.

### BLOG MODEL:
Blog Model fields are title,slug(-title url for seo and unique), category, author, featured_image,short description, blog body, status(),is_featured,created_at,updated_at

ForeignKey --> which is used to make connection between category model and blog and on_cascade delete blog if that particular category is deleted

### Propoulate Slugs:
To generate or automate slug url with title we must use admin class with propulated_filels

class BlogAdmin(admin.ModelAdmin):

  propoulated_field = { 'slug' : (title,)}


### Admin Table list display
add  list display in blogadmin class

list_display = ('title', category','author', 'status', 'is_featured',)

add search filed-- search_fileds = ('id', 'title', 'category', 'status')

for category we can't put foreign key like that so we need to make category__category_name

for status also we had named o,1 so change that to draft and published and change integerfield to charField

list_editable = ('is_featured',)