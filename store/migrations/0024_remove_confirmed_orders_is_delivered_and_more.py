# Generated by Django 4.2.2 on 2023-06-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_confirmed_orders_is_delivered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmed_orders',
            name='is_delivered',
        ),
        migrations.AddField(
            model_name='confirmed_orders',
            name='status',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
