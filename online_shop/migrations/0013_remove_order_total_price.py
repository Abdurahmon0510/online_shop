# Generated by Django 5.0.7 on 2024-08-03 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0012_alter_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
