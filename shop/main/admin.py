from django.contrib import admin
from .models import *


class AdminProduct(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(SmartPhone, AdminProduct)
admin.site.register(Chainsaw, AdminProduct)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Axe, AdminProduct)
