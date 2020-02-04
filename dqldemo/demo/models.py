from django.db import models

class Dest(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.TextField()

    
    
    def  __str__(self):
        return self.name

