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

add some examples of blogs and categories

### Fetch Categories In HOme Page:

in home view -> categories = Category.objects.all() and import category model and use context and pass to home.html

categories = Category.objects.all()
context = {
  'categories': categories,
}

return render(request, 'home.html', context)

in home.html 

cretae a for loop --> {% for cat in categories %}
 <a> {{ cat }} </a> "here cat will return catogey name because Category model has representaion with __str__ and for other field we must use cat.updated_at"

{%  endfor %}


### Display Featured Posts On The HomePage:

again in home view

featured_posts = BLog.objects.filter(is_featured = True,status='Published') . order_by('updated_at')

pass this featured_posts to context

we use for loop in template to grab all featured posts

{% for post in featured_posts %}


{% endfor %}

when we try this we will get all featured_posts one by one but it don't look good we use if condition to one feature_post 

{% if forloop.first %}

it will loop only first featured_post not all

 {%endif%}

 and make changes of all title, things

 for remaining featured posts create a sub heading and create normal like posts seeeing on up

 same code like above 

 for date we use post.createdt_at and for timesince like 1 hour ago like that we use | it acts has a filter --> {{ post.created_at | timesince }} ago

 again add if condition for not repeating first one 

 {% if not forloop.fist %}

 {% endif %}

 change featured post image 

 {{post.featured_image.url}} --> dynamic url


 ### Display Remaing post which are not featured post

 same process repeat it with featured_post == False and status condition == 'Published"

 for short_description use filter | turncatewords:25

 to reduce short descrption words to stay consistency page


 ### Foreign Key RelationShips: (many to one relation)

 ids connection

category = models.ForeignKey(Category, on_delete=models.CASCADE)

Here Category Model Field has many items but for one blog post we can select only one category so here many to one relationship works well. 

### Inside DataBase:

The Conections depends on ids for example Sports category it has specific category_id(pk) automatic generated by django and blog has ids so the selecting categories of ids in backend.

In Django, every record in the database automatically gets a primary key (ID).
So when we create a Category (like Sports, Tech, etc.), Django gives each one a unique id.

When we create a Blog Post, it stores the category’s ID, not the text name.

This means:

The Blog model has a Foreign Key field,That field references the Category table,The relationship is based on the category’s ID and This allows Django to link blogs to categories efficiently.

### 🧠 Why Django Uses IDs Instead of Names

IDs never change,Names might change (e.g., “Sports” → “Sport News”),Databases are optimized for ID lookups and Ensures referential integrity.
So even if the category name changes and the relationship with blogs still works fine.


author = models.ForeignKey(User, on_delete=models.CASCADE)

An author can write many blog posts but a blog post can only be written by ONE author.


### POSTS BY CATEGORY:

create a url when some when comes with category we need to move to blogs_app

path('category/', include('blogs_app.urls'))

import include and cretae urls.py file in blogs_app

import path from urls and add urlpatterns = [

path('<int:category_id>/', views.blogs_by_category, name = 'blogs_by_category')
]

In views write logic --> for only specific blogs category = category_id

def posts_by_category(request, category_id):
  posts = Blog.objects.filter(status='published', category = category_id)
  context = {
    'posts' : posts,
  }
  return render(request, 'posts_by_category.html', context)

  ### display blogs by category

  design posts_by_category.html

 ### 404 custome error page:

 create 404.html template and create with any error with  number

 create a p tag with the category does't work and  in settings set debug= False and allowed_host= '*'

change settings to back

### Template Inheritance:To Avoid Same Structure of Html

The Common html contect like  heading,footer,navbar, links for every page and to avoid the same copy or html structure we can avoid the same code for everypage by using template inheritance 


create a template base.html and a html file containes header,main,footer here header and footer  are same content for every page

copy and paste header and footer in base and for main part we use blocks

{% block content %}

{% endblock %}

we use extend to base.html to work

{% extends 'base.html' %} --To use base.html structure in other templates

{% block content %}

Main Content Goes Here the all html structures

{% endblock %}

### Context Process:

We pass context dictionary to only specific html file in views by storing like a dictionary but we can use context process here which works well and don't need to repeat same line of code and It takes as a request like url and pass dictionary

make an module in app like views.py,urls.py with context_processors.py the spelling should be correct

create a function

def get_categories(request):
  categories = Category.objects.all()
  return dict(categories = categories)

to work this function we need to configure some settings --> templates --> context_processors --> add path 

"appname.context_processors.function name"

the navbar with categories will show on every page now

### Linking Posts by Category Url :

in nav of base.html for a tag where categories have use href =' {% url 'posts_by_categoy' cat.id %}'

### Single Blog Page Setup: a Blog on full page with full details:

1.First : Urls -> path('<slug:slug>', views.)

import views from blogs app --> from blogs import views as BlogViews --> path("<slug:slug>", BlogViews.blogs, name ="blogs"),

in app level views define view

def blogs(request, slug):
  return render(request, 'blog.html')

extends base.html

in home for read more tag add href to 'blogs' post.slug 

and when we click on read more or continue reading the view function gets request and data so we can get that to blogs in views to featch blog

single_blog = get_object_or_404(Blog, slug=slug, status = 'published')

context = { ' single_blog': single_blog}

### ABout PAGE:

create app and 

try:
    about = About.objects.get()
  except:
    about = "none"

Here try block only works for get method and when we add 2 abouts or or filter,all methods won't work and after adding one data disable the add about button again by overiding model admin

class AboutAdmin(admin.ModelAdmin):
  
  def has_add_permission(self,request):

    count = About.objects.all().count()

    if count == 0:

      return True

    return False

### Search Filter:

in base.html header 

create a div with specific cols and add div for input_group and form action to get

we getting search function first(method ="get") and later we submit so here Method is get(first)

for action we create a url to submit data


path ("blogs/search/", BlogsView.search , name ="search")

view is going to be in app level

def search(request):
  return render(request, 'search.html')

create search template:

Write Logic First to featch blogs by search terms:

def search(request):
  keyword = request.GET.get('keyword') ## This keyword comes from input search we have mention that name = 'keyword' in input search bar(check html )

  blogs  = Blogs.objects.filter(title_icontains=keyword) ## here i(works for casesentive upper or lower anything) and contains(if the keyword has in title)
  
  blogs = Blog.objects.filter(title__icontains = keyword , status = "published") (here we have using comma means and condition(both must be true) but we need to use or to search in short description or body blog)

  now we have problem in search we can't fetch for short description,body search to overcome we have a Q(from db.models import first)

from django.db.models import Q -- now we will see how to use

  blogs = Blog.objects.filter(Q(title_icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body__icontains = keyword), status = "published" )

  we pass conntext to search template

use posts_by_category template fro frontend and keep value = {{keyword}} in input tag to see which term we have searched to display


### Registration SetUp:

create url for register a user and create view with render register.html 

by using model form we are going use existed forms by django and cretae a forms.py file in to in project level not app

use django default user model from django.contrib.auth.models import user 

class RegistrationForm(CreateUserForm):

import CreateUserForm from django.contrib.auth.forms UserCreateForm

and inside that create class Meta:

    model = User
    fileds = ("email", 'username', 'password1', 'password2') ## password1(password) and password2(confrim password)

import this form to views and start and pass context to register.html

Install django cripsy form using documentation and bootstrap4 cripsy form and make sure to configure settings

load crispy_forms_tags in register template and use like or {{ form | crispy }} thats it

Now The Form is Loading with action register and when we click on submit the data is going to save in request.POST method so if the request.method == POST we get data we validate the form data and registration id done successfully and for else case we render form 

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

## LOGIN Functionality:

create url path with login name = login

cretae view with login and render login.html

check the connectoin 

and to authenticate user we have built in django  AuthenticationForm from forms and import it and authentication has 2 fileds by defalut (username,password) and register also but we have added email field extra 

and 

def login(request):
  if request.method == "POST"
  form = AuthenticationForm(request, request.POST)
  if form.is_valid():
  username= form.cleaned_data['username'] ## cleaned_data(dict) post method stores values in dict and is_valid function validates the data and stored in dict.so we use  cleaned_data['username]
  password = form.cleaned_data['password'] # featching details of user to check and to check or authenticate we have built in model auth.authenticate and import auth from contrib
  user = auth.authenticate(username=username, password=password)
  if user is not None:
    auth.login(request,user)
  return redirect('home')

  form = AuthenticationForm()
  context = {
    'form': form,
  }
  return render(request, 'login.html', context)

### LogOut Functionality:

when the useer logged we see that login and register is still visiable. If user is not logged in we can show login and register else case we display logout with user name in base.html chnage the syntext

            <a href="" class="text-dark m-1 ">{{ user }} </a>  ## user comes from context_processors by default
 
create a path for logout 

def logout(request):
  auth.logout(request)
  return redirect("home")

### 🔍 Quick Example Flow
Before logout

user logs in

Django creates session

browser keeps session cookie

After logout

Django deletes session

cookie no longer valid

user becomes Anonymous


### AUthentication and Authrization

Authentication:Checks user credentials and give permission to system 

Authrization:What kind of permissions did user have(like admin,staff,editor like that)

create user with staff status(can login to admin page) and check permissions and permissions are generated when we migrate models some default models which are auth,admin and 

Default permissions where created when we cretae models for our project and every model has 4 types of permission(edit,delete,view,create)

Groups: The groups are used to create a set permissions and this group of permissions can be given to users by just selecting grop editor group,manager group.



### Upgrading Packages:

pip freeze > requirments.txt # creates all packages to file requirements  change == to >=

pip install -r requirments.txt --upgrade # -r recursively 

### Managers and Editors DashBoard 

create an app Dashboards and add app name in installed settings

cretae path for dashboard and include dashboards.urls

create a url in dashboards for empyty path

