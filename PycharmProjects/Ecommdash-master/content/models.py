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

class Product(models.Model):
    # catId = models.IntegerField()
    name = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=10)
    date = models.DateField(null=True)
    desc = models.CharField(max_length=120, null=True)
    image = models.ImageField(upload_to='content/productimages', default="")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name