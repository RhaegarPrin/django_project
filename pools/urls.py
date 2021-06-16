from django.urls import path
from . import urls
from . import views
from . import employee_view
urlpatterns = [
    path('', views.index, name = 'Pools'),
    path('home/', views.home, name = 'home'),
    path('result/', views.getAll, name='result'),
    path('register/', views.register,  name = 'register'),
    path('products/', views.products, name = 'products'),
    path('login/' , views.login , name = 'login'),
    path('search/' , views.search , name = 'search'),
    path('filter' , views.filter , name = 'filter'),
    path('products/product_cmt/' , views.product_comment , name = 'product_cmt'),
    path('products/add_cmt/', views.add_cmt , name = 'products/add_cmt'),
    path('products/view_cart/', views.viewCart, name = 'products/add_cmt'),
    path('products/view_bills/', views.view_bills , name = 'products/view_bills'),
    path('order/', views.order, name = 'order'),
    path('products/view_cart/address/', views.address, name = 'address'),
    path('detail/', views.detail, name = 'detail'),

    path('employeelogin', employee_view.login, name = 'employelogin'),
    path('warehouse', employee_view.warehouse, name = 'warehouse'),
    path('add', employee_view.add, name = 'add'),
    path('sales', employee_view.sales, name = 'sales')

]