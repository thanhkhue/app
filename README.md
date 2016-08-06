# App - a demo how django combine with AngularJS

## Install virtual environt:

** If you're not installed pip, run this **

    sudo apt-get install python-pip
**Follow instruction below**
    
    [sudo] pip install virtualenv

    virtualenv env

    source env/bin/activate
    
    bower install

**Run Django project **

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver


**Open your browser: localhost:8000/places_list**

**The angular files is stored in jobs/static/jobs/src/service**

**To see the tree of project, see app/app/urls.py**