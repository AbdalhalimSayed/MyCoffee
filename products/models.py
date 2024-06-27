from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.PositiveIntegerField()
    photo=models.ImageField(upload_to="Photo/%y/%m/%d")
    is_active=models.BooleanField(default=True)
    publishDate=models.DateTimeField(default=datetime.now())
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering=["id"]
    
    
