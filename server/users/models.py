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

class SocialMediaInfo(models.Model):
    profile = models.OneToOneField(Profile, verbose_name=_("Social Media"), related_name="socialMedia", on_delete=models.CASCADE)
    website = models.CharField(_("Website"), max_length=255, blank=True, null=True)
    facebook = models.CharField(_("Facebook"), max_length=255, blank=True, null=True)
    twitter = models.CharField(_("Twitter"), max_length=255, blank=True, null=True)
    linkedin = models.CharField(_("Linkedin"), max_length=255, blank=True, null=True)
    instagram = models.CharField(_("Instagram"), max_length=255, blank=True, null=True)
    stackoverflow = models.CharField(_("Stackoverflow"), max_length=255, blank=True, null=True)
    github = models.CharField(_("Github"), max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.profile.user}'


class Skill(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Skill"),related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(_("Skill Name"), max_length=250)

    def __str__(self):
        return self.name


class Education(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"),related_name="educations", on_delete=models.CASCADE)
    degree = models.CharField(_("Degree"), max_length=150)
    institution = models.CharField(_("Institution"), max_length=255)
    session = models.CharField(_("Session"), max_length=50)

    def __str__(self):
        return f'{self.profile.user} {self.degree}'


