from . models import *
from django.shortcuts import render , redirect
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse , JsonResponse
from .models import *

def login(request):
	if request.method == 'POST'  :
		print('-------------- insi 	')
		login_status = False
		try :
			employee = Employee.objects.get(userName = request.POST.get('userName') , passWord = request.POST.get('passWord'))
			print(request.POST.get('userName') )
			print(request.POST.get('passWord'))
			print(Employee)
			if employee.position == 'warehouse' :
				print('warehouse----')
				return redirect('warehouse')
			if employee.position == 'sales' :
				print('sales----')
				return redirect('sales') 
			return render(request, 'http://localhost:8000/admin/')
		except :
			print('except')
			return render (request, 'Employee/employee_login.html' )
	else :
		print('sffsfdsfs')
		print(request.GET.get('userName') )
		return render (request, 'Employee/employee_login.html' )
	return redirect('products')

def warehouse (request) :
	print('goin ware house')
	if request.method== 'GET' :
		items = Items.objects.all
		return render (request , 'Employee/warehouse.html' , {'items' : items} )
		
	if request.method == 'POST' :
		item_id = request.POST.get('item_id')
		item_name=request.POST.get('name')
		item_price=request.POST.get('price')
		item_quantity = request.POST.get('quantity')
		item = Items.objects.get(item_id=item_id)
		if item.iteem_name != item_name :
			item.iteem_name = item_name
		if item.item_price != item_price :
			item.item_price = item_price
		item.item_quantity += int(item_quantity)
		item.item_note='update'
		item.save()	

		return redirect ('warehouse')

def sales (request) :
	if request.method=='GET':
		items = Items.objects.filter(item_note='update')
		return render (request, 'Employee/sales.html',{'items' : items})
	if request.method=='POST':
		item_id = request.POST.get('item_id')
		item=Items.objects.get(item_id=item_id)
		try :
			product = Products.objects.get(item_fk=item_id)
			product.product_name=item.iteem_name
			product.product_price=item.item_price
			product.product_quantity += item.item_quantity
			product.save()
			item.item_note='updated'
			item.item_quantity=0
			item.save()
			return redirect('sales')
		except :
			Products(item_fk=item_id , product_name=item.iteem_name , product_price=item.item_price , \
				product_quantity=item.item_quantity, product_tags=item.item_tags, product_img=item.item_img).save()
			item.item_note='updated' 	
			item.save()
			return redirect('sales')
	return render (request, 'Employee/sales.html')

def add(request):
	if request.method=='GET':
		name = request.GET.get('name')
		price= request.GET.get('price')
		quantity=request.GET.get('quantity')
		img = request.GET.get('img')
		tag = request.GET.get('tag')
		item= Items(iteem_name=name , item_price=price ,item_note='update' , item_quantity=quantity , item_img=img , item_tags=tag, )
		item.save()
		return redirect('warehouse')
		
