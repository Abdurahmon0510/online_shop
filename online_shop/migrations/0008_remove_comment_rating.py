# Generated by Django 5.0.7 on 2024-08-01 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0007_comment_is_provide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
    ]
