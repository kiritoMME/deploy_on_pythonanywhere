# Generated by Django 4.2.2 on 2023-06-12 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0015_alter_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='confirmed_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100000)),
                ('phone', models.CharField(max_length=15)),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='store.order')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
