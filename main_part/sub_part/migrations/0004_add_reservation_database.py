# Generated by Django 3.2.5 on 2021-08-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0003_add_package_database'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_reservation_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=100)),
                ('dt_from', models.CharField(max_length=100)),
                ('dt_to', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('security', models.CharField(max_length=100)),
                ('deposit', models.CharField(max_length=100)),
                ('tax', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('borrow', models.CharField(max_length=100)),
                ('back', models.CharField(max_length=100)),
            ],
        ),
    ]
