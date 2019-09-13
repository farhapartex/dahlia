## Blog CMS 1.0

`Blog-CMS` is for creating blog just by adding contents. `Blog-CMS` provide various type of API such which is essential for a blog website.

### Prerequisite

* Python 3
* Docker

### Installation

* Clone the git repository
* Enter the folder `blog-cms`
* Open terminal in this folder
* For first setup run `docker-compose build server`
* After run `docker-compose up server`
* Open another terminal in same folder
* Run the command on second terminal `docker-compose exec server bash`
* Run the command on second terminal `pipenv run ./manage.py migrate` ( It will create database schema for the CMS)
* Run the command on second terminal `pipenv run ./manage.py createsuperuser` ( By this command you will create account for the CMS as superuser. Provide `username`, `password` and `email`)
* Open browser and hit the url `127.0.0.1:8000/admin`. It will redirect to the CMS admin login page. 