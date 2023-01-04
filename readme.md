# REST API Crash Course - Introduction + Full Python API Tutorial

## All about interfaces
- Application Programming Interface - any software with distinct function
- REST - Representational state Transfer

## HTTP Methods
1. GET - Retrieve
2. POST - Write (new data)
3. DELETE - Delete
4. PUT - Write (update data)

Softwares must be CRUD - Create, Read, Update, Delete

POST /drinks -> for creating, kaya we don't have the ID
PUT /drinks/605 -> for updating, kaya we have the ID
> POST creates a new one. So it can duplicate. PUT updates, so it can't duplicate.

# Stackoverflow Sample
http://api.stackexchange.com/2.3/answers?order=desc&sort=activity&site=stackoverflow

# Setting up Flask
Unix: export FLASK_APP=app
Windows CMD: set FLASK_APP=app
Windows PowerShell: env:FLASK_APP="app"

then, flask run

So for our case:
1. Navigate to venv, activate it
2. Go to this folder
3. set FLASK_APP=POSTflask.py
4. set FLASK_ENV=development