from django.db import models

# Create your models here.

class productCategoy(models.Model):
    Categoryname = models.CharField(max_length=30)

    def __str__(self):
        return self.Categoryname


class locations(models.Model):
    locationname = models.CharField(max_length=30)

    def __str__(self):
        return self.locationname


class shopName(models.Model):
    name=models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    shopLocation= models.ForeignKey(locations,on_delete=models.DO_NOTHING)


class productShop(models.Model):
    productname = models.CharField(max_length=40)
    productCategory = models.ForeignKey(productCategoy,on_delete=models.DO_NOTHING)
    shop = models.ForeignKey
