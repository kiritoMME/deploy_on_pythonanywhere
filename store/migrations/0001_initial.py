# Generated by Django 4.2.2 on 2023-06-30 20:27

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(blank=True, max_length=600)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000000)),
                ('sizes', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('rate', models.FloatField(default=5)),
                ('rate_text', models.CharField(default='FFFFF', max_length=5)),
                ('featured_product', models.BooleanField(default=False)),
                ('offer', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='static/images/product-null.jpg', null=True, upload_to='static/images/')),
                ('gallery_1', models.ImageField(blank=True, default='static/images/product-null.jpg', null=True, upload_to='static/images/')),
                ('gallery_2', models.ImageField(blank=True, default='static/images/product-null.jpg', null=True, upload_to='static/images/')),
                ('gallery_3', models.ImageField(blank=True, default='static/images/product-null.jpg', null=True, upload_to='static/images/')),
                ('gallery_4', models.ImageField(blank=True, default='static/images/product-null.jpg', null=True, upload_to='static/images/')),
                ('offer_image', models.ImageField(blank=True, null=True, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('comment', models.CharField(default='this is from django default comment elit. Quis, repellat. Id natus aut, quasi unde voluptatum, ipsa fugit esse enim numquam officiis cupiditate repellendus nihil fuga. A iure fugit hic. lo', max_length=1000000)),
                ('rate_text', models.CharField(default='FFFFF', max_length=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='confirmed_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=100000)),
                ('phone', models.CharField(default='', max_length=15)),
                ('total_price', models.FloatField()),
                ('status', models.CharField(default='pending', max_length=20)),
                ('orders', models.ManyToManyField(to='store.order')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
