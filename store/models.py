from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=600, blank=True)
    def __str__(self):
        return self.username

class product(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000000)
    sizes = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    rate = models.FloatField(default=5)
    rate_text = models.CharField(max_length=5,default='FFFFF')
    featured_product = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/images/', default='static/images/product-null.jpg' ,blank=True, null=True)
    gallery_1 = models.ImageField(upload_to='static/images/',default='static/images/product-null.jpg' ,blank=True, null=True)
    gallery_2 = models.ImageField(upload_to='static/images/',default='static/images/product-null.jpg' ,blank=True, null=True)
    gallery_3 = models.ImageField(upload_to='static/images/',default='static/images/product-null.jpg' ,blank=True, null=True)
    gallery_4 = models.ImageField(upload_to='static/images/',default='static/images/product-null.jpg' ,blank=True, null=True)
    offer_image = models.ImageField(upload_to='static/images/',blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class testimonial(models.Model):
    name = models.CharField(max_length=500)
    comment = models.CharField(default="this is from django default comment elit. Quis, repellat. Id natus aut, quasi unde voluptatum, ipsa fugit esse enim numquam officiis cupiditate repellendus nihil fuga. A iure fugit hic. lo",max_length=1000000)
    rate_text = models.CharField(max_length=5,default='FFFFF')
    image = models.ImageField(upload_to='static/images/',blank=True, null=True)

    def __str__(self):
        return f'{self.name} Testimonial.'

class order(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(product, default=None, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    count = models.IntegerField()
    is_confirmed = models.BooleanField(default=False)
    # confirmed_order = models.ForeignKey(confirmed_orders)
    
    def __str__(self):
        return f'{self.user.username} -->  {self.product} ({self.size})'

class confirmed_orders(models.Model):
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE)
    address = models.CharField(max_length=100000, default="")
    phone = models.CharField(max_length=15, default="")
    total_price = models.FloatField()
    orders = models.ManyToManyField(order)
    orders2 = models.ManyToManyRel(orders, order)
    status = models.CharField(default='pending', max_length=20)

    def __str__(self):
        return f'{self.user.username} ===== {self.status} '
