from django.db import models


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='content/catimages',default="")
    status = models.BooleanField()

    def __str__(self):
        return self.name

class subcategory(models.Model):
    catId = models.IntegerField()
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='content/subimages',default="")
    status = models.BooleanField()

    def __str__(self):
        return self.name

class product(models.Model):
    subcatId = models.IntegerField()
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    quantity = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    image = models.ImageField(upload_to='content/ProductsImg',default="")
    status = models.BooleanField()

    def __str__(self):
        return self.name