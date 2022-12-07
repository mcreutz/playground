### Create / initialize a project
django-admin startproject <name>

### Create an app within a project
python manage.py startapp <name>

### Run the dev server
python manage.py runserver

## Migrations are modifications in the data model

### Make migrations
python manage.py makemigrations

### Apply to the database
python manage.py migrate

### create an admin user account
python manage.py createsuperuser