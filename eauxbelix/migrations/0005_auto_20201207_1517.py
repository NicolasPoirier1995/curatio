# Generated by Django 3.1.3 on 2020-12-07 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201207_1257'),
        ('eauxbelix', '0004_auto_20201207_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boiler',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client'),
        ),
    ]