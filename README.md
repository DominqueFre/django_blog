# django_blog



## Steps for Django project setup
    Select python version and the appropriate versions of other apps...
-Start a venv 
    `python -m venv .venv`
-Install python version required
-Create 
--a .python-version file
    input version only eg. 3.12
--a env.py file 
    to include SECRET_KEY and DATABASE_URL
--a .gitignore 
    to include env.py and .venv
--a Procfile  
    used in conjunction with gunicorn and Heroku to launch web wsgi processes.


**Install**
`pip install jjjjj~=1.23.0`
Django              (framework)
    (also installs asgiref, tzdata, sqlparse)
psycopg2            (postgresql database)
    (also installs setuptools)
dj-database-url     (postgresql database)
gunicorn            (web launcher heroku)
django-summernote   (adds functionality eg filtering capability)
    (also installs webencodings and bleach)
whitenoise          (hmmm CSS, images )

Create a requirements.txt file
    `pip freeze --local >requirements .txt`

### Steps for creating project 
Create a project
    `django.admin start project xxx`
Create apps
    `python manage.py startapp yyy`
Include in Installed apps
Create a view
Include in URL's

### Steps for setting up django's key safely
In the projects settings.py file


In the env.py file


### Steps for setting up database URL safely
In the projects settings.py file - utilising the imported env from the key.
    `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
In the env.py file

### Steps for database information     
Create models in apps in models.py
Once created use manage.py
    `python manage.py makemigrations yyy`
    `python manage.py migrate yyy`
Inside yyy/admin.py - register the model(s)
    `from .models import zzz`
    `admin.site.register(zzz)`
Inside settings under the database information (this is similar to allowed hosts...)
`CSRF_TRUSTED_ORIGINS = ["https://*.codeinstitute-ide.net/","https://*.herokuapp.com"]`

### Steps for completing the installation of summernote
In the projects settings.py file - in INSTALLED APPS
    `django_summernote`
In the projects urls.py file - add the path
    `path('summernote/', include('django_summernote.urls)),`
In the admin.py file  - of the app that will use summernote add the import 
    `from django_summernote.admin import SummernoteModelAdmin`
Then in the same file add a decorator and class 
(replaces a simple registration eg admin.site.register(ModelClassName))
`@admin.register(ModelClassName)`
`class PostAdmin(SummernoteModelAdmin):`
    `list_display = ('aaaaa', 'slug', 'status')`
    `search_fields = ['aaaaa']`
    `list_filter = ('status',)`
    `prepopulated_fields = {'slug': ('aaaaa',)}`
    `summernote_fields = ('content',)`
Apply the migrations for the django_summernote app
`python manage.py migrate`
