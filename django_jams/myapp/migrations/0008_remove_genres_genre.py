# Generated by Django 4.2 on 2023-04-06 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_artist_albums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genres',
            name='genre',
        ),
    ]