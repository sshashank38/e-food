# Generated by Django 3.0.4 on 2020-07-20 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='delivery_date',
        ),
    ]
