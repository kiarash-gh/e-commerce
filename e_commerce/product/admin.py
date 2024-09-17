from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductImages,
    ProductSpecification,
    Specification,
    Tag
)
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(ProductSpecification)
admin.site.register(Specification)
admin.site.register(Tag)