# Generated by Django 4.2.5 on 2023-09-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Dob', models.DateField()),
                ('Email', models.CharField(max_length=100)),
                ('Mob', models.IntegerField()),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]