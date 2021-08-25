# Generated by Django 3.2.5 on 2021-07-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='reg1',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]