# Generated by Django 3.1 on 2020-08-29 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('url', models.URLField(verbose_name='url')),
                ('pending', models.BooleanField(default=False, verbose_name='pending')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='LinkTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.link', verbose_name='link')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.tag', verbose_name='tag')),
            ],
            options={
                'verbose_name': 'link x tag',
                'verbose_name_plural': 'link x tag',
                'unique_together': {('link', 'tag')},
            },
        ),
        migrations.AddField(
            model_name='link',
            name='tags',
            field=models.ManyToManyField(through='links.LinkTag', to='links.Tag'),
        ),
        migrations.AddField(
            model_name='link',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
