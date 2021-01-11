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
- Create database 
```
psql postgres
postgres=# create database <database_name>;
CREATE DATABASE
CREATE USER <username> WITH PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```
-Update `mini_mpulse/sensitive_settings.py` file with local postrgres DB credentials. Populate `SECRET_KEY` with something super secret.
- Run migrations
```
python manage.py migrate
```
- Create yourself as a superuser and add your `USERNAME` and `PASSWORD` to `mini_mpulse/sensitive_settings.py`
```
python manage.py createsuperuser
Username: <username>
Email: <email (if you want, or skip)>
Password: **********
Password (again): *********
Superuser created successfully.
```
## Start app
- Start Django app
```
# from /mini-mpulse
source venv/bin/activate
python manage.py runserver
```
- Now visit `http://127.0.0.1:8000/admin/` and login using the superuser credentials you created! 

## Test APIs
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/eac83d52514bd1b5655b#?env%5B00%20-%20Mini-Mpulse-User%5D=W3sia2V5IjoidXNlcm5hbWUiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoicGFzc3dvcmQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoiYWNjb3VudF9pZCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJtZW1iZXJfaWQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoicGhvbmVfbnVtYmVyIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6ImNsaWVudF9tZW1iZXJfaWQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9XQ==)

## Future Development
- For CSV Uploader: 
-- Extend Django Admin and showcase button there
-- Generate output file showing success/fail including any error messages
-- Keep db record of filenames and timestamps
-- Display csv uploads via clickable links so user can access the upload stats

- Optimize batch inserts to handle files with up to 5 million rows
-- Include Celery and RabbitMQ to handle processing large files while also servicing other requests
-- Split file into multiple files and save to a location with adequate memory
-- Spawn processes for each file using multiple workers
-- API rate limiting and throttling
-- Incorporate que and system performance checks/calls
-- Possible create separate API specifically for CSV uploads separate from main application APIs

- Dockerize

