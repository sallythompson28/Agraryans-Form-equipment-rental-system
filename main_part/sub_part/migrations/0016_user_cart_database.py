# Generated by Django 3.2.5 on 2021-08-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0015_check_user_drill_database'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_cart_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('borrow', models.CharField(max_length=100)),
                ('back', models.CharField(max_length=100)),
            ],
        ),
    ]
