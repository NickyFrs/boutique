from django.contrib import admin
from .models import Product, Category

# Register your models here.
<<<<<<< HEAD

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
=======
admin.site.register(Product)
admin.site.register(Category)
>>>>>>> origin/main
