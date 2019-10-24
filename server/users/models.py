from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Permission
from media_browser.models import MediaImage

# Create your models here.


def profile_photo_upload_path(instance, filename):
    return "dp/{0}".format(filename)


ROLE_CHOICE = ((1, "Administrator"), (2, "Moderator"), (3, "Editor"))


class UserRole(models.Model):
    role = models.SmallIntegerField(_("User Role"), choices=ROLE_CHOICE, default=1)

    def __str__(self):
        if self.role == 1:
            return f"Administrator"
        elif self.role == 2:
            return f"Moderator"
        elif self.role == 3:
            return f"Editor"
        elif self.role == 4:
            return f"Subscriber"


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        related_name="profile",
        on_delete=models.CASCADE,
    )

    avatar = models.ForeignKey(
        MediaImage,
        verbose_name=_("Profile Image"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    bio = models.CharField(_("Bio"), max_length=150, blank=True, null=True)
    about = models.TextField(_("About"),blank=True, null=True)
    mobile = models.CharField(_("Mobile"), max_length=15, blank=True, null=True)
    user_role = models.ForeignKey(
        UserRole,
        verbose_name=_("User Role"),
        related_name="profile",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user}"


SOCIAL_TYPE = (
    (1, "Facebook"),
    (2, "Linkedin"),
    (3, "Github"),
    (4, "Stackoverflow"),
    (5, "Behance"),
    (6, "Kaggle"),
    (7, "Flicker"),
)


class SocialMediaInfo(models.Model):
    profile = models.ForeignKey(
        Profile,
        verbose_name=_("Social Media"),
        related_name="socialMedias",
        on_delete=models.CASCADE,
    )
    type = models.SmallIntegerField(_("Type"), choices=SOCIAL_TYPE, default=1)
    url = models.CharField(_("URL"), max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.profile.user} {self.type}"


class Skill(models.Model):
    profile = models.ForeignKey(
        Profile,
        verbose_name=_("Skill"),
        related_name="skills",
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("Skill Name"), max_length=250)

    def __str__(self):
        return self.name


class Education(models.Model):
    profile = models.ForeignKey(
        Profile,
        verbose_name=_("Profile"),
        related_name="educations",
        on_delete=models.CASCADE,
    )
    degree = models.CharField(_("Degree"), max_length=150)
    institution = models.CharField(_("Institution"), max_length=255)
    session = models.CharField(_("Session"), max_length=50)

    def __str__(self):
        return f"{self.profile.user} {self.degree}"

