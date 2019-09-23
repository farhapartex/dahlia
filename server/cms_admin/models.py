from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class SystemPermission(models.Model):
    name = models.CharField(_("Permission"), max_length=250)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(_("Menu Text"),max_length=255)
    url = models.CharField(_("Menu URL"),max_length=255)
    allow_submenu = models.BooleanField(choices=((True,"Yes"),(False,"No")), default=False)
    parent_menu = models.ForeignKey('self', related_name='submenus', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
    




