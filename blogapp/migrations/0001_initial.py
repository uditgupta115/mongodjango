# Generated by Django 2.2.1 on 2019-08-19 10:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ManyToManyField(to='blogapp.Account')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='blogapp.Publication')),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
        migrations.AddField(
            model_name='account',
            name='profile_status',
            field=models.ManyToManyField(blank=True, to='blogapp.Status'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ManyToManyField(related_query_name='user_model', to=settings.AUTH_USER_MODEL),
        ),
    ]
