from django.db import models
from django.contrib.auth.models import AbstractUser



class Adress(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone_number=models.CharField(max_length=13,null=True,blank=True)
    region = models.ForeignKey(Adress, on_delete=models.CASCADE, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable= 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Product(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Sub_Category', on_delete=models.PROTECT)
    brand = models.ForeignKey('Brend', on_delete=models.PROTECT, null=True, blank=True)
    color = models.ManyToManyField(to='Color', blank=True)
    photos = models.ManyToManyField(to='Image')
    quantity = models.IntegerField(default=0)
    futures = models.TextField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sale = models.BooleanField(default=False)
    old_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descount_percent = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_banner = models.BooleanField(default=False)
    is_delive = models.BooleanField(default=False)
    reting = models.FloatField(default=0)
    size = models.ForeignKey(to='Size', on_delete=models.PROTECT)
    create_at = models.DateField(auto_now=True)




class Category(models.Model):
    name = models.CharField(max_length=55)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now=True)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Brend(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    img = models.ImageField(upload_to='color-photo/')
    name = models.CharField(max_length=255)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    img = models.ImageField(upload_to='photos_img/')


class Size(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Card(models.Model):
    user = models.ForeignKey(to=User, on_delete= models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    quaertity = models.IntegerField
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Saved(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE)
    product = models.ManyToManyField(to='Product')

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    is_delivery = models.BooleanField(default=False)
    extra_phone_number = models.CharField(max_length=13, null=True, blank=True)
    payments_type = models.BooleanField(default=True)
    ofice_number = models.ForeignKey(to=Adress, on_delete=models.PROTECT)
    lat = models.FloatField()
    lot = models.FloatField()
    create_at = models.DateField(auto_now=True)




class Ofice(models.Model):
    name = models.CharField(max_length=25)
    number = models.IntegerField()
    region = models.ForeignKey(to=Adress, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now=True)




