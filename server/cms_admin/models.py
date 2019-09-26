from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class SystemPermission(models.Model):
    name = models.CharField(_("Permission"), max_length=250)

    def __str__(self):
        return self.name