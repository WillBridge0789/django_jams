# Generated by Django 4.2 on 2023-04-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_genres_genre_alter_songs_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='albums',
            field=models.ManyToManyField(to='myapp.album'),
        ),
    ]
