from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

'''
Models:
Post, Comment, React, Tag
'''

class Category(models.Model):
    name = models.CharField(_("Category"), max_length=150)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name =models.CharField(_("Tag"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return self.name

PUBLISH_CHOICE = ((True,"Publish"),(False,"Not Publish"))
class Post(models.Model):
    title = models.CharField(_("Title"), max_length=150)
    subtitle = models.CharField(_("Sub Title"), max_length=250, blank=True, null=True)
    body = models.TextField(_("Post"))
    category = models.ForeignKey(Category, verbose_name=_("Category"), related_name="posts", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name=_("Tags"))
    published = models.BooleanField(_("Published"), choices=PUBLISH_CHOICE, default=False)

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return self.title

REACT_TYPES = ((1,"LIKE"),(2,"DISLIKE"),(3,"CLAP"),(4,"LOVE"))
class React(models.Model):
    post = models.ForeignKey(Post, verbose_name=_("Post"),related_name="reacts", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(_("Amount"))
    type = models.SmallIntegerField(_("Type"), choices=REACT_TYPES, default=1)

    def __str__(self):
        return f'{self.post} {self.amount}'


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=_("Post"),related_name="comments", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", verbose_name=_("Parent"),related_name="children", on_delete=models.SET_NULL, blank=True, null=True)
    body = models.TextField(_("Comment Text"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return f'{self.post} {self.body[:30]}' 
