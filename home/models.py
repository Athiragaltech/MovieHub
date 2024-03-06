from django.db import models

class movie(models.Model):
    name=models.CharField(max_length=100)
    director=models.CharField(max_length=100)
    screen=models.CharField(max_length=100)
    img = models.ImageField(upload_to ='uploads/') 
