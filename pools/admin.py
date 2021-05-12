from django.contrib import admin
from . models import Members
from . models import Products
from . models import order_products
from . models import product_cmt
from . models import bill
# Register your models here.
admin.site.register(Members)
admin.site.register(Products)
admin.site.register(order_products)
admin.site.register(product_cmt)
admin.site.register(bill)