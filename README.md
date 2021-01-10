# mini-mpulse
"Mini mPulse" Python-Django application that utilizes APIs, Celery and Redis to manage members 

## Local Setup
 - Clone repo locally
 - Create virtual environment and install python libraries
```
cd mini-mpulse
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Create database and update file with local postrgres DB credentials
- Run migrations
```
python manage.py migrate
```

## Start app
- Start Django app
```
# from /mini-mpulse
source venv/bin/activate
python manage.py runserver
```

## Test APIs
- Postman Collection: (Collectoin Link)[]

## Future Development


