# Generated by Django 3.2 on 2021-07-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhandler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_form',
            name='age',
            field=models.IntegerField(),
        ),
    ]