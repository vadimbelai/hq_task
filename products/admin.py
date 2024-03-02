from django.contrib import admin

from .models import Product, Lesson, ProductAccess, Group

admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(ProductAccess)
admin.site.register(Group)