# A Multi User Data Entry Application
This is a RESTful API for a multiuser data entry application.  
The API allows for multiple categories of data, including 
Health Institutions, Professional Details, and Event Details, with the option to add additional categories as needed. 

# Core Technologies and Libraries Used

Technology/Library | Description 
--- | --- |
*Django REST Framework* | *Api building framework for django*
*Postman* |*Api testing*
*Unittest* | *A python library for writing tests*
*Postgres* | *A relational database service*
*Python* | *An object oriented programming language* 
*Redis* | *An in mem0ry cache service*
*Django* | *A python framework for building serverside applications*
*Flake8* | *A code formatting library for Python*  
  

# Setting up the codebase locally

This is a step by step guide on how to set up the codebase locally

Clone the project
----------------------
``` shell
git clone https://github.com/Euniceatieno/Data-Entry-App.git
```
Set up your virtual environment
----------------------
``` shell
gpython3 -m venv env
```
Activate your virtual environment
----------------------
``` shell
source env/bin/activate
```
Install the required packages
----------------------
``` shell
python3 -m pip install -r requirements.txt --no-cache-dir
```
Create a .env file with the following environment variables
------------------------------------------------------------------
``` shell
SECRET_KEY=yoursecretkey
DATABASE_NAME=yourdb
DATABASE_USER=yourdbuser
DATABASE_PASSWORD=yourbdpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
Export your environment variables
--------------------------------------------
``` shell
source .env
```
Create a local database with the credentials in your .env file
---------------------------------------------------------------

Run migrations
----------------------
``` shell
python3 manage.py makemigrations
```
Migrate database updates
----------------------
``` shell
python3 manage.py migrate
```
Run Unit Tests
----------------------
``` shell
coverage run manage.py test

```
Start local server
----------------------
``` shell
python3 manage.py runserver
```
Swagger Technical Documentation
----------------------
``` shell
http://127.0.0.1:8000/data_entry_app/swagger/

```
# Contacts
For any queries ,reach out to *eunniceatieno@gmail.com*
