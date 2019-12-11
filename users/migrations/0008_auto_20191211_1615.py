# Generated by Django 2.2 on 2019-12-11 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191018_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='cart',
            name='nearest_landmark',
            field=models.TextField(blank=True, null=True, verbose_name='nearest landmark'),
        ),
        migrations.AddField(
            model_name='cart',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')], verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='cart',
            name='second_address',
            field=models.TextField(blank=True, null=True, verbose_name='second address'),
        ),
    ]
