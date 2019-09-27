from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class SiteInformation(models.Model):
    site_name = models.CharField(_("Site Name"), max_length=150)

    def __str__(self):
        return self.site_name


class MenuItem(models.Model):
    name = models.CharField(_("Menu Text"), max_length=255)
    url = models.CharField(_("Menu URL"), max_length=255)
    allow_submenu = models.BooleanField(
        choices=((True, "Yes"), (False, "No")), default=False
    )
    parent_menu = models.ForeignKey(
        "self",
        related_name="submenus",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    site = models.ForeignKey(
        SiteInformation,
        verbose_name=_("Site"),
        related_name="menus",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    seen = models.BooleanField(choices=((True,"Seen"),(False,"Not Seen")),default=False,blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

