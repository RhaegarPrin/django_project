from django.urls import path
from . import urls
from . import views
urlpatterns = [
    path('', views.index, name = 'Pools'),
    path('home/', views.home, name = 'home'),
    path('result/', views.getAll, name='result'),
    path('register/', views.register,  name = 'register'),
    path('products/', views.products, name = 'products'),
    path('login/' , views.login , name = 'login'),
    path('products/search/' , views.search , name = 'search'),
    path('products/product_cmt/' , views.product_comment , name = 'product_cmt'),
    path('products/add_cmt/', views.add_cmt , name = 'products/add_cmt'),
    path('products/view_cart/', views.viewCart, name = 'products/add_cmt'),
    path('products/view_bills/', views.view_bills , name = 'products/view_bills'),
    path('order/', views.order, name = 'order')
]