"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from users import views as u_views
from blog import views as b_views
from sites import views as s_views
from media_browser import views as media_views

admin_router = DefaultRouter()
public_router = DefaultRouter()

# public routers
public_router.register(r"profile", u_views.PublicProfileViewSet)
public_router.register(r"categories", b_views.PublicCategoryViewSet)
public_router.register(r"tags", b_views.PublicTagViewSet)
public_router.register(r"posts", b_views.PublicPostViewSet)
public_router.register(r"comments", b_views.PublicCommentViewSet)
public_router.register(r"reacts", b_views.PublicReactViewSet)
public_router.register(r"site", s_views.PublicSiteAPIView)
public_router.register(r"contact", s_views.ContactCreateAPIView)

admin_router.register(r"medias", media_views.MediaImagePrivateAPIView)

urlpatterns = [
    path("django/admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view()),
    path("cms/", include("cms_admin.urls")),
    re_path(r"^api/v1/admin/", include(admin_router.urls)),
    re_path(r"^api/v1/public/", include(public_router.urls)),
]

handler404 = "cms_admin.views.error_404_view"
# handler500 = "cms_admin.views.Error404Page"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

