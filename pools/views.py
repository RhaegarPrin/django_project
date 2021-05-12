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
		return render (request, 'pools/login.html')
	else:		
		return render( request , 'pools/register.html')
# Them product vao cart ( chua thanh toan)
def add2Cart(mem_id , product_id , product_price, total ,order_date , order_status):
		product = Products.objects.get(product_id= product_id)
		product.product_quantity -= int(total) 
		product.save()
		print(mem_id , product_id , product_price , total , order_date , order_status) 
		order = order_products( Member_id = mem_id , product_id =  product_id , product_price = product_price ,total=  total,\
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
	if request.method == 'POST':
		mem_id=value
		product_id = request.POST.get('product_id')
		product_price = request.POST.get('product_price')
		quantity = request.POST.get('quantity')
		order_date = datetime.today()
		order_status = 0;
		print(' order :   ', mem_id , product_id , product_price , quantity , order_date , order_status) 
		add2Cart( mem_id , product_id , product_price , quantity , order_date , order_status) 
		return render(request, 'pools/prodcuts.html', {'user' : user ,'all_products' : all_products , 'member_id' : mem_id } )
	else :
		print('GET')
		return render(request, 'pools/prodcuts.html', {'user' : user ,  'all_products' : all_products , 'member_id' : value } )


def search(request ) :
	mem_id = request.COOKIES.get('id')	
	user = request.COOKIES.get('user')
	if request.method == 'POST' :
		name = request.POST.get('key_word')
		list_product = Products.objects.filter(product_name = name)
		if list_product == None :
			return redirect( 'products' )
		return render(request, 'pools/prodcuts.html', {'user' : user ,'all_products' : list_product , 'member_id' : mem_id } )
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
def product_comment(request ):
	if request.method == 'GET' :
		all_cmt = product_cmt.objects.all()
		product_id = request.GET.get('product_id')
		print('ok cmt' , product_id )
		list_cmt = []
		print(type(all_cmt))
		for cmt in all_cmt :
			if int(product_id) == cmt.product_id  : 
				print('matched ' , cmt.cmt )
				list_cmt.append(cmt)
		print( type(list_cmt), 'all : ', list_cmt)
		return render(request , 'pools/product_cmt.html', {'all_cmt':list_cmt} )
	return redirect( 'products' )

def add_cmt( request) :
	if request.method == 'POST' :
		product_id = request.POST.get('product_id')
		cmt = request.POST.get('cmt')
		Member_id = 1
		product_cmt_action =  product_cmt(Member_id  = Member_id , product_id = product_id , cmt = cmt)
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

	return render (request , 'pools/cart.html', {'cart' : cart})

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
		new_bill = bill( Member_id=member_id , total=0 , order_date=current_date)
		new_bill.save()
		return new_bill

def order(request) :
	if request.POST.get('action')=='post':
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
		new_bill = create_bill(member_id)
		for item in all :
			print(item.id)
			if  (str(item.id) in res )  == False:
				total += item.total*item.product_price
				item.order_status = new_bill.id + 1
				item.save()
				list_payment.append(item)
				print(item, 'saved')
		new_bill.total = total
		new_bill.save()
		list = order_products.objects.filter(Member_id=member_id , order_status= 0)
		#filter by id in msg 
		print(list)
		#data = serializers.serialize('json', list_payment)
		#print(data)
		#return redirect('products')
	return render (request, 'pools/home.html' )


