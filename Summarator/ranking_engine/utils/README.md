Summarator
==========


Running
-------


```bash
$ rabbitmq-server
$ celery -A Summarator worker -l info
$ python manage.py runserver
```


API Endpoints
-------------


### Updating database

@api {get} /scrape/DOMAIN

Example:

```bash
$ curl -H "Content-Type: application/json" -X GET http://localhost:8000/scrape/tech
```

### Processing new data

@api {get} /process

Example:

```bash
$ curl -H "Content-Type: application/json" -X GET http://localhost:8000/process
```