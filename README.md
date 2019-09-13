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

### Available API endpoints

* `api/v1/public/profile` ( This API will expose blog admin information)
* `api/v1/public/categories` ( This API will expose blog category list)
* `api/v1/public/categories/id` ( This API will expose blog single category. Here `id` is number)
* `api/v1/public/tags` ( This API will expose blog tags for various type posts)
* `api/v1/public/tags/id` ( This API will expose blog tags for various type posts. Here `id` is a number)
* `api/v1/public/posts` ( This API will expose blog post list)
* `api/v1/public/posts/id` ( This API will expose single blog post. Here `id` is a number)