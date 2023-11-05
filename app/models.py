from django.db import models

# Create your models here.
class Computer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    files = models.FileField(upload_to='files')
    
    def __str__(self):
        return self.name