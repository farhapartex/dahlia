# Generated by Django 2.1.12 on 2019-09-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_education'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmediainfo',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='socialmediainfo',
            name='github',
        ),
        migrations.RemoveField(
            model_name='socialmediainfo',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='socialmediainfo',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='socialmediainfo',
            name='stackoverflow',
        ),
        migrations.RemoveField(
            model_name='socialmediainfo',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='socialmediainfo',
            name='website',
        ),
        migrations.AddField(
            model_name='socialmediainfo',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'Facebook'), (2, 'Linkedin'), (3, 'Github'), (4, 'Stackoverflow'), (5, 'Behance'), (6, 'Kaggle'), (7, 'Flicker')], default=1, verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='socialmediainfo',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL'),
        ),
    ]
