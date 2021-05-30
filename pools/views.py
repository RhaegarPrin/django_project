from django.shortcuts import render , redirect
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse , JsonResponse
from datetime import datetime

from . models import Members
from . models import Products 
from . models import order_products
from . models import product_cmt
from . models import bill
from . models import funds
from . models import * 
import json
#from .form import Memberform

from django.views.decorators.csrf import csrf_exempt
#index va home lam cho vui
def index(request):
    return HttpResponse("Index")
def home(request):
	if request.POST.get('action')=='post':
		print('----------------Hmmmmmmmmmmmmmmm')
		msg = request.POST.get('msg')
		jsondata={}
		jsondata['msg']=msg
		return JsonResponse(jsondata)
	return render (request, 'pools/home.html' )

# tra ve toan bo object member
def getAll(request):
		all_members = Members.objects.all
		return render (request , 'pools/result.html' , {'all':all_members})
#dang ky 
def register(request):
	if request.method == "POST":
		#form = Memberform( request.POST or None)
		#if form.is_valid() :
		#form.save()
		us =  request.POST.get('userName')
		passw =  request.POST.get('password')
		em =   request.POST.get('name')
		n = request.POST.get('email')
		print( passw)
		mem = Members( userName = us , passWord = passw ,name = n , email = em)
		print(mem.passWord)
		mem.save()
		mem_fund = funds(Member_id=mem.id , fund=0)
		mem_fund.save()
		return render (request, 'pools/login.html')
	else:		
		return render( request , 'pools/register.html')
# Them product vao cart ( chua thanh toan)
def add2Cart(mem_id , product_id , product_price, total ,order_date , order_status):
		product = Products.objects.get(product_id= product_id)
		product.product_quantity -= int(total) 
		product.save()
		print(mem_id , product_id , product_price , total , order_date , order_status) 
		order = order_products( Member_id = Members.objects.get(id=mem_id) , product_id = Products.objects.get(product_id= product_id) , product_price = product_price ,total=  total,\
			order_date = order_date , order_status = order_status  )
		order.save()
#Tra ve trang san pham da order
def products(request  ):
	all_products = Products.objects.all
	print('log in call', request.method)
	#set cookies cho user
	value = request.COOKIES.get('id')	
	user = request.COOKIES.get('user')
	print('cookie id : ' , value)
	print('cookie user : ' , user)
	fund = funds.objects.get(Member_id = value)
	if request.method == 'POST':
		mem_id=value
		product_id = request.POST.get('product_id')
		product_price = request.POST.get('product_price')
		quantity = request.POST.get('quantity')
		order_date = datetime.today()
		order_status = 0;
		print(' order :   ', mem_id , product_id , product_price , quantity , order_date , order_status) 
		add2Cart( mem_id , product_id , product_price , quantity , order_date , order_status) 
		return render(request, 'pools/prodcuts.html', {'user' : user ,'all_products' : all_products , 'member_id' : mem_id, 'fund' : fund } )
	else :
		print('GET')
		return render(request, 'pools/prodcuts.html', {'user' : user ,  'all_products' : all_products , 'member_id' : value , 'fund' : fund } )


def search(request ) :
	mem_id = request.COOKIES.get('id')	
	user = request.COOKIES.get('user')
	if request.method == 'GET' :
		name = request.GET.get('msg')
		print("name :::: " , name) ;
		list_product = Products.objects.filter(product_name__contains = name)
		print ( list_product)
		data = serializers.serialize('json', list_product)
		return JsonResponse ( {"data" : data })
	return redirect( 'products' )
#login
def login(request):
	if request.method == 'POST'  :
		all_members = Members.objects.all()
		for mem in all_members :
			if( request.POST.get('userName') == mem.userName and request.POST.get('passWord') == mem.passWord) :
				print(mem)
				response = redirect('products')
				response.set_cookie('id', mem.id)
				response.set_cookie('user', mem.name)
				return response
			else :
				print('false')
	return render (request, 'pools/new_login.html')
# tra ve tat ca comment cua member co product = product_id
def product_comment(request  ):
	if request.method == 'GET' :
		product_id = request.GET.get('product_id')
		all_cmt = product_cmt.objects.filter(product_id=product_id)
		print('ok cmt' , product_id )
		return render(request , 'pools/product_cmt.html', {'all_cmt':all_cmt} )
	return redirect( 'products' )

def add_cmt( request) :
	if request.method == 'POST' :

		product_id = request.POST.get('product_id')
		cmt = request.POST.get('cmt')
		member_id =  request.COOKIES.get('id')
		print(member_id)
		product_cmt_action =  product_cmt(Member_id  =Members.objects.get(id=member_id), product_id =Products.objects.get (product_id = product_id ), cmt = cmt)
		product_cmt_action.save()
		return redirect('products')
	return redirect('products')

def viewCart(request) :
	member_id = request.POST.get('member_id')
	print(member_id)
	value = request.COOKIES.get('id')
	print('mem id ' , value)
	cart = order_products.objects.filter(Member_id=value,order_status=0)
	print("cart  :  ", cart)

	return render (request , 'pools/cart.html', {'cart' : cart, 'mem_id':value})

def view_bills(request) :
	member_id = request.POST.get('member_id')
	print(member_id)
	value = request.COOKIES.get('id')
	print('mem id ' , value)
	bills = bill.objects.filter(Member_id=value)
	print("bills  :  ", bills)
	return render (request , 'pools/bill.html' , {'bills' : bills})

#xu ly order , tao bill

from django.core import serializers

def create_bill(member_id):
		current_date = datetime.today()
		new_bill = bill( Member_id=Members.objects.get(id=member_id), total=0 , order_date=current_date)
		new_bill.save()
		return new_bill

def update_fund(member_id , total) :
	if total <= 0 :
		return False
	fund = funds.objects.get(Member_id = member_id)
	if( fund.fund >= total and total > 0) :
		fund.fund -= total 
		fund.save()
		return True
	return False 

def order(request) :
	print(request.method)
	if request.method=='POST':
		msg = request.POST.get('msg')
		msg = msg.replace('[',"")
		msg = msg.replace(']',"")
		print(type(msg))
		print(msg)
		res = msg.split(',')
		print('res : ' , res )
		member_id  = request.COOKIES.get('id')
		all = order_products.objects.filter(Member_id=member_id,order_status=0)
		print(all)
		list_payment=[]
		total = 0
		chosen_items = []
		result = "false"
		for item in all :
			print(item.id)
			if  (str(item.id) in res )  == False:
				total += item.total*item.product_price
				chosen_items.append(item)
		if	update_fund(member_id , total)	== True :
			address = Address.objects.filter(Member_id=member_id)[0]
			employee= Employee.objects.get(id=1)

			print('total = ',total)
			new_bill = create_bill(member_id)
			for item in chosen_items :
				item.order_status = new_bill.id + 1
				item.save()
				result= "true"
			new_bill.total = total
			new_bill.save()
			shipping(bill_fk= new_bill , Employee_fk=employee , Address_fk=address).save()
			list = order_products.objects.filter(Member_id=member_id , order_status= 0)
			print(list )
			print(result)
			address = Address.objects.filter(Member_id = member_id)
			print(address)
			addr = serializers.serialize('json', address)
			return JsonResponse( {"data":result  , "address" : addr , "bill_id" :str(new_bill.id)} )
		# print('DATA : ',data)
		return JsonResponse( {"data":result  , "address" : addr } )
	return render (request, 'pools/home.html' )

def detail(request):
	print('called')
	if request.method=='POST':
		msg = request.POST.get('msg')
		msg = msg.replace('"',"")
		print(type(msg),'-----------',msg)
		ship_detail= shipping.objects.get(bill_fk=msg)
		status = ship_detail.status 
		address = Address.objects.filter(id=ship_detail.Address_fk.id)
		bil_id = int(msg)+1
		list_order = order_products.objects.filter(order_status=bil_id)
		for item in list_order :
			print(item.id,"- " , item.total, " - " , item.product_price)

		data = serializers.serialize('json', list_order)
		address_json = serializers.serialize('json', address)
		print(data)
		return JsonResponse( {"data" : data , "address" : address_json , "status" : status} )
def filter(request):
	if request.method == 'GET' :
		tag = request.GET.get('msg')
		print(type(tag))
		print('filter by' + tag)		
		list_product = Products.objects.filter(product_tags__contains = tag)
		print(list_product)
		data = serializers.serialize('json', list_product)
		return JsonResponse ( {"data" : data })
	return redirect('products')

def address(request) :
	if request.method=="POST":
		mem_id =  request.POST.get('mem_id');
		bill_id =  request.POST.get('bill_id');
		city_ = request.POST.get('city');
		district_ = request.POST.get('district');
		house_ = request.POST.get('house');
		print( mem_id , city_ , district_ , house_)
		add = Address.objects.filter(Member_id=mem_id , city=city_ , district = district_ , house=house_)
		if add.exists() :
			print("0--------" ,add)
		else :
			print('none')
			address =Address(Member_id= Members.objects.get(id=mem_id) , city=city_ , district = district_ , house=house_)
			address.save()
			ship_with_other_address = shipping.objects.get(bill_fk=bill_id)
			ship_with_other_address.Address_fk= address
			ship_with_other_address.save()
		return redirect('products')

