# Generated by Django 2.2 on 2019-09-07 08:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(blank=True, max_length=15)),
                ('reposts_count', models.PositiveIntegerField(blank=True)),
                ('comments_count', models.PositiveIntegerField(blank=True)),
                ('attitudes_count', models.PositiveIntegerField(blank=True)),
                ('followers_count', models.PositiveIntegerField(blank=True)),
                ('verified_type', models.IntegerField(blank=True)),
                ('source', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('-source',),
            },
        ),
        migrations.CreateModel(
            name='DataShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtitle', models.CharField(max_length=150)),
                ('dcontent', models.TextField()),
                ('disposition', models.NullBooleanField()),
                ('dcreated', models.TimeField(default=django.utils.timezone.now)),
                ('dupdate', models.DateTimeField(auto_now=True)),
                ('dclass', models.CharField(blank=True, max_length=150)),
                ('durl', models.URLField(blank=True)),
                ('dsource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamanager.DataSource')),
            ],
            options={
                'ordering': ('-dcreated',),
            },
        ),
    ]