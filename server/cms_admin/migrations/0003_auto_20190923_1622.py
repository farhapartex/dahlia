# Generated by Django 2.1.12 on 2019-09-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_admin', '0002_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='allow_submenu',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]