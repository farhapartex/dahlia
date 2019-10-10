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
  * [Category, Tag](https://github.com/farhapartex/dahlia#category-tag)
  * [Post](https://github.com/farhapartex/dahlia#post)
  * [User Role](https://github.com/farhapartex/dahlia#user-role)
  * [Site Information](https://github.com/farhapartex/dahlia#site-information)
  * [Main Menu](https://github.com/farhapartex/dahlia#main-menu)
  * [API Reference](https://github.com/farhapartex/dahlia#api-refrence)
  * [Contact Message](https://github.com/farhapartex/dahlia#contact-message)
  

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
* Creating User with role

## Feature Description of Dahlia

### Category, Tag
In **Dahlia**, you can create category, tag. `Administrator` can create, update and delete any category or tag. `Moderator` only can add and edit. `Editor` only can edit any tag or category.

### Post
In **Dahlia**, the main purpose is creating blog post easily and maintain the blog site. A post is a combination of title, subtitle, post content, category and tags. A post can contain multiple tags. `Administrator` can create , update and delete any post. `Moderator` can create new post and update an existing post. But can not delete any post. `Editor` can only edit any post.

### Media
In **Dahlia**, images are stored separately. In **Dahlia**, any kind of images will be used from the **Media** section. `Administrator` and `Moderator` can add, update and delete any image. `Editor` only can view image.

#### User Role
**Dahlia** provides 3 user role which are `Administrator`, `Moderator` and `Editor`. In **Dahlia**, `Administrator` can do any kind of operations, `Moderator` can also perform any kind of operations without creating user, deleting any information and changing system information.

### Site Information
**Dahlia** give user chance to create their blog site information such as, site name, site logo, site favicon etc. Only `Administrator` can add or edit site information.

### Main-Menu
**Dahlia** allow you to create menu list for your blog website. Remember that, a menu can be created if and only if there is a site information created before. Without creating site information, you can not create any menu in **Dahlia**.

### API Reference
**Dahlia** provides various types of API to integrate in front-end template to show the post content. Here are list of APis in **Dahlia**

* `"/api/v1/public/profile/"` this API will expose profile information of the `Administrator`. **Dahlia** consider that `Administrator` is the owner of the blog site.
* `"/api/v1/public/categories/"` this API will expose all category list which are available in **Dahlia**
  * Category API support filtering category. User can filter category by category name
  * With filtering option the API will look as `"/api/v1/public/categories/?category_name="`
  * Category API also support pagination. For each call Post API give 10 category.
* `"/api/v1/public/tags/"` this API will expose all tag list which are available in **Dahlia**
  * Tag API support filtering tags. User can filter tags by category name
  * With filter option the API is `"/api/v1/public/tags/?tag_name="`
  * Tag API also support pagination. For each call Post API give 10 tag.
* `"/api/v1/public/posts/"` this API will expose all post list which are public only.
  * Post API support filtering. User can filter data by using title, subtitle or post content.
  * With filter option the API is `"/api/v1/public/posts/?title=&subtitle=&body="`
  * Post API also support pagination. For each call Post API give 10 post content.
* `"/api/v1/public/site/"` this API will expose site information

Full list of API can be found in API menu which is under Settings

### Contact Message
**Dahlia** provides a way to connect reader with the blog owner. Reader of the blog site can send a message via a public post API which is `"/api/v1/public/contact/"`. This API is only for post data. No one can use the API for get request. Reader must have to provide their name, email with the message. 

In **Dahlia** owner will get notifications alert for unseen contact messages which will be shown in the upper right corner of header.
