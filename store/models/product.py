from django.db import models
from .category import Category



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default=" ")
    image = models.ImageField(upload_to='uploads/products/')
    # category_name = Category.objects.all(id)

    def __str__(self):
        return f"{self.name}"
    
    # def __str__(self):
    #     return f"{self.category_name}"
