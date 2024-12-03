from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
    image=models.ImageField(upload_to="Category_images",null=True,blank=True)


class ProductDB(models.Model):
    category=models.CharField(max_length=100,null=True,blank=True)
    pname=models.CharField(max_length=100,null=True,blank=True)
    pprice=models.IntegerField(null=True,blank=True)
    pdescription=models.CharField(max_length=500,null=True,blank=True)
    pimage=models.ImageField(upload_to="Product_images",null=True,blank=True)
