# Generated by Django 4.0.2 on 2022-02-10 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userinformationadmin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInformationAdmin',
        ),
    ]