Django Course Project – Alison

Overview

This repository contains the practical projects and exercises completed during the Django Fundamentals – The Fast Track course on Alison. The course teaches how to build web applications using the Django framework, covering everything from setup to deployment.


Features

Fully functional Django project with apps

Uses Model-View-Template (MVT) architecture

Includes admin interface, ORM, templates, and views

Demonstrates CRUD operations and database handling

Built-in security features: CSRF, SQL injection prevention, password hashing


Skills Learned

Setting up Django projects and applications

Working with Django models, views, and templates

Using the Django admin interface

Handling user authentication and password hashing

Securing web applications with Django’s built-in protections

Understanding the “batteries included” philosophy


Installation

Clone the repository:

git clone https://github.com/Kitoonka/django-course.git

Navigate to the project folder:

cd djangoDemo

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the server:

python manage.py runserver

Access the application at http://127.0.0.1:8000/

Project Structure
djangoDemo/
│
├── myApp/           # Main Django application
├── manage.py        # Django management script
├── db.sqlite3       # Database file
└── djangoDemo/      # Project settings and URLs
