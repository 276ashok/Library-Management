# Generated by Django 4.2.5 on 2023-09-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_signup',
            name='Dob',
            field=models.CharField(max_length=20),
        ),
    ]
