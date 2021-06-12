from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class productCategoy(models.Model):
    Categoryname = models.CharField(max_length=30)

    def __str__(self):
        return self.Categoryname


class locations(models.Model):
    locationname = models.CharField(max_length=30)

    def __str__(self):
        return self.locationname


class shopDetail(models.Model):
    shopOwner = models.CharField(max_length=40)
    shopName=models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    shopLocation= models.ForeignKey(locations,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.shopName

class productShop(models.Model):
    productname = models.CharField(max_length=40)
    productDescription = models.TextField()
    productCategory = models.ForeignKey(productCategoy,on_delete=models.DO_NOTHING)
    shop = models.ForeignKey(shopDetail,on_delete=models.CASCADE)

    def __str__(self):
        return self.productname
