# Generated by Django 2.2 on 2019-04-10 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileobject',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
