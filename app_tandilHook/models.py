from django.db import models

# Create your models here.

class Lure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    image = models.ImageField(upload_to='app_TandilHook/images/lures', verbose_name='Image', null=True)
    type = models.CharField(max_length=100, verbose_name='Type')
    description = models.TextField(verbose_name='Description', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', null=True)
    
    def __str__(self):
        product = "Item: " + self.name + " - " + "Description: " + self.description
        return product
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
    
class Cloth(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    image = models.ImageField(upload_to='app_TandilHook/images/clothing/', verbose_name='Image', null=True)
    type = models.CharField(max_length=100, verbose_name='Type')
    size = models.CharField(max_length=100, verbose_name='Size')
    description = models.TextField(verbose_name='Description', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', null=True)

    def __str__(self):
        product = "Item: " + self.name + " - " + "Description: " + self.description
        return product
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

class Tool(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    image = models.ImageField(upload_to='app_TandilHook/images/tools/', verbose_name='Image', null=True)
    type = models.CharField(max_length=100, verbose_name='Type')
    description = models.TextField(verbose_name='Description', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', null=True)

    def __str__(self):
        product = "Item: " + self.name + " - " + "Description: " + self.description
        return product

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()