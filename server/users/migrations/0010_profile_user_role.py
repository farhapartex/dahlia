# Generated by Django 2.2.5 on 2019-10-02 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_userrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to='users.UserRole', verbose_name='User Role'),
        ),
    ]
