from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=200)
    item = models.CharField(max_length=200, default='')
    price = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    #name = models.CharField(max_length=300)

    #def __str__(self):
        #return self.item

class Electronics(models.Model):
    name = models.CharField(max_length=200)
    item = models.CharField(max_length=200, default='')
    price = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    #name = models.CharField(max_length=300)

#  Stores

class Stores(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')


class ElJubilazo(models.Model):
    name = models.CharField(max_length=200)
    item = models.CharField(max_length=200, default='')
    price = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')

class Vefase(models.Model):
    name = models.CharField(max_length=200)
    item = models.CharField(max_length=200, default='')
    price = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')



    def __str__(self):
        return self.item