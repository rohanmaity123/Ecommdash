from django.contrib import admin
from .models import category,subcategory,Product

admin.site.register(category)
# Register your models here.


admin.site.register(subcategory)
admin.site.register(Product)