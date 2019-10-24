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
    path(
        "medias/<int:mid>/change",
        login_required(MediaBrowserUpdateView.as_view()),
        name="media_update",
    ),
    path(
        "medias/<int:mid>/delete",
        login_required(MediaDeleteView.as_view()),
        name="media_delete",
    ),
    path("users/", login_required(UserListView.as_view()), name="users"),
    path("users/add/", login_required(UserListView.as_view()), name="user_add"),
    path(
        "users/<int:uid>/update/",
        login_required(UserUpdateView.as_view()),
        name="user_update",
    ),
    path(
        "users/<int:uid>/delete/",
        login_required(UserDeleteView.as_view()),
        name="user_delete",
    ),
    path(
        "users/<int:uid>/password/update/",
        login_required(UserPasswordUpdateView.as_view()),
        name="password_update",
    ),
    path(
        "users/<int:uid>/profile/",
        login_required(ProfileView.as_view()),
        name="profile",
    ),
    path(
        "users/<int:uid>/profile/add/",
        login_required(ProfilePostView.as_view()),
        name="profile_post",
    ),
    path(
        "users/<int:uid>/profile/update/",
        login_required(ProfileUpdateView.as_view()),
        name="profile_update",
    ),
    path(
        "users/<int:uid>/education/post/",
        login_required(EducationPostView.as_view()),
        name="education_post",
    ),
    path(
        "users/<int:uid>/social/post/",
        login_required(SocialPostView.as_view()),
        name="social_post",
    ),
    path(
        "users/<int:uid>/skill/post/",
        login_required(SkillPostView.as_view()),
        name="skill_post",
    ),
    path("site/", login_required(SiteView.as_view()), name="site"),
    path(
        "site/<int:siteid>/change/",
        login_required(SiteUpdateView.as_view()),
        name="site_update",
    ),
    path(
        "site/<int:siteid>/delete/",
        login_required(SiteDeleteView.as_view()),
        name="site_delete",
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
    path(
        "comments/<int:notifyid>/view/",
        login_required(CommentView.as_view()),
        name="comment_view",
    ),
    path(
        "comments/<int:comment_id>/delete/",
        login_required(CommentDeleteView.as_view()),
        name="comment_delete",
    ),
    path("apis/", login_required(APIUrlListView.as_view()), name="apis"),
    path(
        "permissions/", login_required(PermissionListView.as_view()), name="permissions"
    ),
    path(
        "permissions/role/<int:role_id>/",
        login_required(PermissionRoleWiseListView.as_view()),
        name="permissions_filter",
    ),
    # url(
    #     r"^(?P<role_id>\w+)/$",
    #     login_required(PermissionListView.as_view()),
    #     name="permissions_filter",
    # ),
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
    # path(
    #     "permissions/<int:role_id>/json-view/",
    #     login_required(UserRolePermissionAPIView.as_view()),
    #     name="permission_list",
    # ),
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
    path("roles/", login_required(UserRoleView.as_view()), name="roles"),
    path("notifications/", login_required(NotificationListView.as_view()), name="notifications"),
    path("notifications/<int:notiid>/delete/", login_required(NotificationDeleteView.as_view()), name="notification_delete"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

