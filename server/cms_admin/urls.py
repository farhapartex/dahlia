from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path("admin/", login_required(HomeView.as_view()), name="home"),
    path("profile/", login_required(ProfileView.as_view()), name="profile"),
    path(
        "categories/<int:catid>/change/",
        login_required(CategoryUpdateView.as_view()),
        name="category_update",
    ),
    path(
        "category/add/", login_required(CategoryAddView.as_view()), name="category_add"
    ),
    path(
        "categories/<int:catid>/delete/",
        login_required(CategoryDeleteView.as_view()),
        name="category_delete",
    ),
    path("categories/", login_required(CategoryView.as_view()), name="category"),
    path("tags/", login_required(TagListView.as_view()), name="tags"),
    path("tags/add/", login_required(TagAddView.as_view()), name="tag_add"),
    path(
        "tags/<int:tagid>/change/",
        login_required(TagUpdateView.as_view()),
        name="tag_update",
    ),
    path(
        "tags/<int:tagid>/delete/",
        login_required(TagDeleteView.as_view()),
        name="tag_delete",
    ),
    path("medias/", login_required(MediaBrowserView.as_view()), name="medias"),
    path("users/", login_required(UserListView.as_view()), name="users"),
    path("users/add/", login_required(UserListView.as_view()), name="user_add"),
    path(
        "users/<int:uid>/profile/",
        login_required(ProfileView.as_view()),
        name="profile",
    ),
    path("site/", login_required(SiteView.as_view()), name="site"),
    path(
        "site/<int:siteid>/change/",
        login_required(SiteUpdateView.as_view()),
        name="site_update",
    ),
    path("menus/", login_required(MenuItemView.as_view()), name="menus"),
    path(
        "menus/<int:mid>/change/",
        login_required(MenuItemUpdateView.as_view()),
        name="menu_update",
    ),
    path(
        "menus/<int:mid>/delete/",
        login_required(MenuItemDeleteView.as_view()),
        name="menu_delete",
    ),
    path("posts/", login_required(PostListView.as_view()), name="posts"),
    path(
        "posts/admin/",
        login_required(PostListAdminAPIView.as_view()),
        name="admin_posts",
    ),
    path("posts/add/", login_required(PostAddView.as_view()), name="post_add"),
    path(
        "posts/<int:pid>/change/",
        login_required(PostUpdateView.as_view()),
        name="post_update",
    ),
    path(
        "posts/<int:pid>/delete/",
        login_required(PostDeleteView.as_view()),
        name="post_delete",
    ),
    path("apis/", login_required(APIUrlListView.as_view()), name="apis"),
    path(
        "permissions/", login_required(PermissionListView.as_view()), name="permissions"
    ),
    path(
        "permissions/<int:permission_id>/change/",
        login_required(PermissionUpdateView.as_view()),
        name="permission_update",
    ),
    path(
        "permissions/<int:permission_id>/delete/",
        login_required(PermissionDeleteView.as_view()),
        name="permission_delete",
    ),
    path("contacts/", login_required(ContactListView.as_view()), name="contacts"),
    path(
        "contacts/<int:cid>/view/",
        login_required(ContactView.as_view()),
        name="contact",
    ),
    path(
        "contacts/<int:cid>/delete/",
        login_required(ContactDeleteView.as_view()),
        name="contact_delete",
    ),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

