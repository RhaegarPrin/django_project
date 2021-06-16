from django.contrib import admin
from . models import *
from . models import Products
from . models import order_products
from . models import product_cmt
from . models import bill
from . models import funds
# Register your models here.
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(order_products)
admin.site.register(product_cmt)
admin.site.register(bill)
admin.site.register(funds)
admin.site.register(Address)
admin.site.register(Employee)
admin.site.register(shipping)
admin.site.register(Items)


