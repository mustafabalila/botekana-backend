# Generated by Django 2.2 on 2019-05-06 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190503_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish_date', models.DateField(verbose_name='finish date')),
                ('percentage', models.PositiveSmallIntegerField(verbose_name='percentage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', related_query_name='discounts', to='products.Product', verbose_name='product')),
            ],
            options={
                'unique_together': {('product', 'finish_date', 'percentage')},
            },
        ),
    ]
