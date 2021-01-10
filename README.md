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
- Create sensitive settings file
```
cp mini_mpulse/sensitive_settings.sample.py mini_mpulse/sensitive_settings.py
```
- Create database and update `mini_mpulse/sensitive_settings.py` file with local postrgres DB credentials. Populate `SECRET_KEY` with something super secret.
- Run migrations
```
python manage.py migrate
```
- Change `DEBUG = True`

## Start app
- Start Django app
```
# from /mini-mpulse
source venv/bin/activate
python manage.py runserver
```

## Test APIs
Please note that when you run in Postman, you will need to set all your environmental variables. Have fun :) 
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/eac83d52514bd1b5655b#?env%5B00%20-%20Mini-Mpulse-User%5D=W3sia2V5IjoidXNlcm5hbWUiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoicGFzc3dvcmQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoiYWNjb3VudF9pZCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJtZW1iZXJfaWQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoicGhvbmVfbnVtYmVyIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6ImNsaWVudF9tZW1iZXJfaWQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9XQ==)

## Future Development


