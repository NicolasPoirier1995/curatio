# Generated by Django 3.1.3 on 2021-04-09 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eauxbelix', '0012_auto_20210409_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watertowerdata',
            name='water_tower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='water_tower_data', to='eauxbelix.watertower'),
        ),
    ]