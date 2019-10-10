## Dahlia 1.0.0

### What is Dahlia
Dahlia is a blog cms, developed based on Django Framework. The main philosophy of `Dahlia` is `no back-end, only front-end`. The purpose is, if user want to host his/her own blog site, they just need to install the cms, and integrate APIs with front-end. It doesn't matter how the front-end will be developed. 

### Prerequisite
* Python 3
* Docker

## Index

* [How To Install](https://github.com/farhapartex/dahlia#how-to-install)
* [Features in Dahlia](https://github.com/farhapartex/dahlia#features-in-dahlia)
* [Features Descriptions](https://github.com/farhapartex/dahlia#description-of-features-in-dahlia)
  * [User](https://github.com/farhapartex/dahlia#user)
  * [Profile](https://github.com/farhapartex/dahlia#user)
  * [Site](https://github.com/farhapartex/dahlia#user)
  * [Main Menu](https://github.com/farhapartex/dahlia#user)

### How To Install

#### First Step
Follow the steps to install dahlia

* Clone the repository and move to the folder `dahlia`
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
* Now click on your username in top of the sidebar , then click on `Profile` tab and provide necessary information and must select `Administrator` from Select Role options and after click on `Submit` button.
* Congratulations! Now you are able to perform all kind of actions in `Dahlia`

### Features in Dahlia

Dahlia is a blog CMS. It provide a user all kind of features which is essential for creating a blog site. The key features are
* Category
* Tag
* Media Browser
* Post
* Public API
* Contact Message
* Menu Options
* Creating User with permissions

## Description of Features in Dahlia

#### User 
Only `Administrator` can create user and control all other features of user (Profile, Education, Skill, Social). `Administrator` and `Moderator` both of them are able to update any user information ( `Moderator` is not able to control `Administrator` profile). But none of them can change password of any user. A password is changeable only by this user which it belongs. 
After creating a user, `Administrator` must have to update profile of that user with proper role. Otherwise, the new user will not be able to do any operations in the CMS.

#### Profile
In `Dahlia`, Profile is a combination of Bio, About, Education ,skill, social and password information. User can add necessary profile information to show in their blog site.

#### Site
Site contains the information of your blog site such as title, site logo, site favicon etc. 

#### Main Menu
A blog site need menus. In `Dahlia` user can create their menu list. To create menu, user must have to create site information before. Otherwise menu can not be created.

