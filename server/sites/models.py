from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class SiteInformation(models.Model):
    site_name = models.CharField(_("Site Name"), max_length=150)

    def __str__(self):
        return self.site_name
