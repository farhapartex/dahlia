## Dahlia 1.0.0

### What is Dahlia
Dahlia is a blog cms, developed based on Django Framework. The main philosophy of `Dahlia` is `no back-end, only front-end`. The purpose is, if user want to host his/her own blog site, they just need to install the cms, and integrate APIs with front-end. It doesn't matter how the front-end will be developed. 

### Prerequisite
* Python 3
* Docker

### How To Install

#### First Step
Follow the steps to install dahlia

* Clone the repository from `https://github.com/farhapartex/dahlia.git`
* Move to the folder `dahlia`
* Open your command shell on this folder
* Type `docker-compose build server`
* Run the command `docker-compose pull server`
* Run the command `docker-compose up server`
* Open another terminal and move to `dahlia` folder
  * Run the command on second terminal `docker-compose exec server bash`
  * Run `pipenv run ./manage.py makemigrations`
  * Run `pipenv run ./manage.py migrate`
* Above command will create migrations file. Now it's time to create superuser
* Run the command in second terminal `pipenv run ./manage.py createsuperuser`
  * Provide `username`, `email` (not necessary), `password` 
* After creating super user open browser and go to `http://127.0.0.1:8000/cms/admin/`
  * It will redirect you to login page
  * Provide username and password to login

#### Second Step
Initially you are not able to perform any operation like Creation, Deletion etc. Initially you are only able to view user list, your own profile , api list and create role section. At left side you will find a sidebar where menus will appear with proper permission means if a user has no permission which need for a menu, the user will not be able to see the menu or the content of the page.

* After installing the most important move is creating roles with permissions
* Click on `Settings` and then `Create Role`. Click on `Add Role` which is on right upper of the page. 
* Dahlia contain 3 roles which are `Administrator`, `Moderator` and `Editor`.
* By Clicking `Add Role` a modal form will appear. Select `Administrator` and select all permissions and submit. 
* Now you are able to perform all kind of actions in `Dahlia`