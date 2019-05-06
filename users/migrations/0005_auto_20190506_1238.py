# Generated by Django 2.2 on 2019-05-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190502_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('c', 'Cash'), ('v', 'Visa')], max_length=2, null=True, verbose_name='payment method'),
        ),
    ]
