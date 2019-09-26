from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
# Create your models here.

def image_upload_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.owner.id, filename)


class MediaImage(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Owner"), related_name='media_images', on_delete=models.CASCADE)
    description = models.CharField(_("Description"),max_length=500, blank=True, null=True)
    height = models.IntegerField(_("Height"), blank=True, null=True)
    width = models.IntegerField(_("Width"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to=image_upload_path, height_field='height', width_field='width', max_length=500)

    def __str__(self):
        return f'{self.owner}-{self.image.name}'