# Generated by Django 3.2.5 on 2021-07-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210726_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produts',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
