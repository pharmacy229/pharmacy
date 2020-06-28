from django.db import models


# Create your models here.
class medicine(models.Model):
    name= models.CharField(max_length=200)
    brand= models.CharField(max_length=200)
    price= models.CharField(max_length=200)
    photo= models.ImageField(upload_to ='images/')
    class Meta:
        db_table="medicine"
    def __str__(self):
        return self.name

class blog(models.Model):
    title= models.CharField(max_length=200)
    detail= models.CharField(max_length=50000)
    name= models.CharField(max_length=200)
    date= models.CharField(max_length=200)
    photo= models.ImageField(upload_to ='images/')
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.name 
        
class subscribe(models.Model):
    email=models.CharField(max_length=200)
    class Meta:
        db_table="subscribe"
    def __str__(self):
        return self.email
        
class contact(models.Model):
    name=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    class Meta:
        db_table="contact"
    def __str__(self):
        return self.name
        
class contactus(models.Model):
    name=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    class Meta:
        db_table="contactus"
    def __str__(self):
        return self.name        
        
class upload(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    image=models.ImageField(upload_to ='images/')
    class Meta:
        db_table="upload"
    def __str__(self):
        return self.name

   
    class Meta:
        db_table="cart"
    def __str__(self):
        return self.name 