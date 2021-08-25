# Generated by Django 3.2.5 on 2021-08-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_auto_20210730_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_package_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('items', models.CharField(max_length=100)),
                ('add_package_file', models.FileField(null=True, upload_to='documents')),
            ],
        ),
    ]