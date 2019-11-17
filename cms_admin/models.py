from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class SystemPermission(models.Model):
    name = models.CharField(_("Permission"), max_length=250)

    def __str__(self):
        return self.name


class Notification(models.Model):
    status = models.BooleanField(_("Status"), default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
