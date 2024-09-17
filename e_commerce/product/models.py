from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    

class Specification(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    original_name = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description= models.TextField(blank=True, null=True)
    tags=models.ManyToManyField(Tag, blank=True)
    #price
    image = models.ImageField(upload_to='media/', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, related_name='product_specifications', on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product} - {self.specification}"
    

class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product} - {self.image}"
    