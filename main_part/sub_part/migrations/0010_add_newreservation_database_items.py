# Generated by Django 3.2.5 on 2021-08-04 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0009_add_newreservation_database'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_newreservation_database',
            name='items',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]