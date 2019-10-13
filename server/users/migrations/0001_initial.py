# Generated by Django 2.2.6 on 2019-10-13 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media_browser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=150, null=True, verbose_name='Bio')),
                ('about', models.TextField(verbose_name='About')),
                ('mobile', models.CharField(blank=True, max_length=15, null=True, verbose_name='Mobile')),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media_browser.MediaImage', verbose_name='Profile Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.SmallIntegerField(choices=[(1, 'Administrator'), (2, 'Moderator'), (3, 'Editor')], default=1, verbose_name='User Role')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(1, 'Facebook'), (2, 'Linkedin'), (3, 'Github'), (4, 'Stackoverflow'), (5, 'Behance'), (6, 'Kaggle'), (7, 'Flicker')], default=1, verbose_name='Type')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='URL')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialMedias', to='users.Profile', verbose_name='Social Media')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Skill Name')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='users.Profile', verbose_name='Skill')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='user_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to='users.UserRole', verbose_name='User Role'),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=150, verbose_name='Degree')),
                ('institution', models.CharField(max_length=255, verbose_name='Institution')),
                ('session', models.CharField(max_length=50, verbose_name='Session')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='users.Profile', verbose_name='Profile')),
            ],
        ),
    ]
