from django.db import models
from cms_admin.forms import *
from .core.models import StreamField
# Create your models here.

class CustomModel(models.Model):
    id = models.AutoField(primary_key=True)
    header = StreamField()
