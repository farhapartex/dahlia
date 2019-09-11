from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

def profile_photo_upload_path(instance,filename):
    return "dp/{0}".format(filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"),related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(_("Avatar"), upload_to=profile_photo_upload_path, blank=True, null=True)
    bio = models.CharField(_("Bio"), max_length=150, blank=True, null=True)
    about = models.TextField(_("About"))
    mobile = models.CharField(_("Mobile"), max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'
