# Generated by Django 3.1.3 on 2020-11-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='author',
        ),
        migrations.AlterField(
            model_name='formation',
            name='video',
            field=models.FileField(unique=True, upload_to='video_formations/'),
        ),
    ]