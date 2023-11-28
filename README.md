# django-practise

This readme is basically the notes I have taken down during this course.
Some commands have been deprecated and I have only included those commands that follows the following versions:

Package Name Version
Django 4.1
Python 3.12.0
debug_toolbar Debug Toolbar 4.2.0

INSTRUCTIONS:

django-admin startproject {{nameoftheproject}} ---> this will create some files under the project name folder that you gave

cd {{nameoftheproject}}

python manage.py startapp {{app_name}}

python manage.py startserver

create project_env using conda before the last one
and do:

conda activate projectenv

---

URL MAPPING

urls.py (firstapp):

from firstapp import views
from django.urls import path

urlpatterns = [
path('',views.help,name="help")
]

urls.py (firstproject):

from django.contrib import admin
from django.urls import path,include
from firstapp import views

urlpatterns = [
path("help/",include('firstapp.urls')),
path('', views.help, name='help'),
path("admin/", admin.site.urls),
]

---

SQL model commands

python manage.py migrate

To register changes:
python manage.py makemigrations {{app name}}
after this migrate the database again

ADMIN INTERFACE:
for easier use, register the model at admin.py file.
from django.contrib import admin
from app.models import Model1, Model2
admin.site.register(Model1)
admin.site.register(Model2)

create a "superuser" to fully use the database and the admin
python manage.py createsuperuser
provide name, email and a password
(use FAKER)
