# Generated by Django 3.2 on 2021-05-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_formpublicdata_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('responses', models.TextField()),
            ],
        ),
    ]
