# Generated by Django 2.1.12 on 2019-09-12 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190912_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediainfo',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialMedias', to='users.Profile', verbose_name='Social Media'),
        ),
    ]