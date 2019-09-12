# Generated by Django 2.1.12 on 2019-09-12 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Twitter')),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Linkedin')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Instagram')),
                ('stackoverflow', models.CharField(blank=True, max_length=255, null=True, verbose_name='Stackoverflow')),
                ('github', models.CharField(blank=True, max_length=255, null=True, verbose_name='Github')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='socialMedia', to='users.Profile', verbose_name='Social Media')),
            ],
        ),
    ]
