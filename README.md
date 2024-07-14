### Follow The Instructions

Pre Requesite 
 - Python

### Install Django

```
pip install django
 ```
### Install Other Dependencies

```
pip install feedparser celery django-celery-beat
```
### Make the database migrate
``` 
cd integratedservices
```
```
python manage.py makemigrations
python manage.py migrate
```

### Make a Super User
 ```
python manage.py createsuperuser
```

### start the server

```
python manage.py runserver
```

Note :
Databases Are Not Filled With any Data Including User Data

Thank You
