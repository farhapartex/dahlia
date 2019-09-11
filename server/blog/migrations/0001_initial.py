# Generated by Django 2.1.12 on 2019-09-11 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Category')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=20, verbose_name='IP Address')),
                ('body', models.TextField(verbose_name='Comment Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(verbose_name='Updated At')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Comment', verbose_name='Parent')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True, verbose_name='Sub Title')),
                ('body', models.TextField(verbose_name='Post')),
                ('published', models.BooleanField(choices=[(True, 'Publish'), (False, 'Not Publish')], default=False, verbose_name='Published')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(verbose_name='Updated At')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.Category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=20, verbose_name='IP Address')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('type', models.SmallIntegerField(choices=[(1, 'LIKE'), (2, 'DISLIKE'), (3, 'CLAP'), (4, 'LOVE')], default=1, verbose_name='Type')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reacts', to='blog.Post', verbose_name='Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tag')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(verbose_name='Updated At')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post', verbose_name='Post'),
        ),
    ]