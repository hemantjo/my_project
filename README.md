# my_project
Step 1- 
  pip install -r requirements.txt

step 2- 
  pip install (location of .whl file I have kept in project folder, where manage.py file is) --------To install mysqlclient

step 3-
Set up your database name and password, and change it accordingly in your settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_schema_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

step 4-
python manage.py makemigrations

step 5- 
python manage.py migrate

step 6- 
python manage.py runserver



