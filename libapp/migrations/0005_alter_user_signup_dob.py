# Generated by Django 4.2.5 on 2023-09-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0004_alter_user_signup_mob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_signup',
            name='Dob',
            field=models.DateField(max_length=20),
        ),
    ]
