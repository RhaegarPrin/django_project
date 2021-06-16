from django.db import models

# Create your models here.
class Customer(models.Model):
	id = models.AutoField(primary_key=True)
	userName = models.CharField(max_length = 100)
	passWord = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	
	def __str__(self):
		return self.userName + ' : ' + self.name

class Employee(models.Model):
	id = models.AutoField(primary_key=True)
	userName = models.CharField(max_length = 100)
	passWord = models.CharField(max_length=100)
	position = models.CharField(max_length=100)

class Address(models.Model):
	Member_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	city = models.CharField(max_length = 100)
	district = models.CharField(max_length = 100)
	house = models.CharField(max_length = 100)
	def __str__(self):
		return str(self.Member_id) + ' City : ' + str(self.city) + " - " + self.district + " - " 
		
class funds(models.Model) :
	id = models.AutoField(primary_key = True)
	Member_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	fund = models.FloatField()
	def __str__(self):
		return str(self.Member_id) + ' fund : ' + str(self.fund)

class Items(models.Model):
	item_id = models.AutoField(primary_key=True)
	iteem_name = models.CharField(max_length=100)
	item_price = models.FloatField()
	item_quantity = models.IntegerField()
	item_note = models.CharField(max_length=1000,null=True)
	item_tags= models.CharField(max_length=1000 , default=None , null=True)
	item_img = models.CharField(max_length=200, default=None, null=True)
	def __str__(self):
		return str(self.item_id) + ': ' + self.iteem_name + ' - ' + str(self.item_price)
class Products(models.Model) :
	item_fk = models.IntegerField(default=None , null=True)
	product_id = models.AutoField(primary_key=True)
	product_name = models.CharField(max_length=100)
	product_price = models.FloatField()
	product_quantity = models.IntegerField()
	product_note = models.CharField(max_length=1000)
	product_tags= models.CharField(max_length=1000 , default=None , null=True)
	product_img = models.CharField(max_length=200, default=None, null=True)
	def __str__(self):
		return str(self.product_id) + ': ' + self.product_name + ' - ' + str(self.product_price)

class order_products(models.Model):
	Member_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
	product_price = models.FloatField()
	total = models.IntegerField()
	order_date = models.DateField()
	order_status = models.IntegerField()
	
	def __str__(self):
		return  str(self.id)+ '----order  :' + 'id member'  + str(self.Member_id) + '- id product :  ' + str(self.product_id)
class product_cmt(models.Model):
	Member_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
	cmt = models.CharField(max_length = 2000)
	
	def __str__ (self):
		return str(self.Member_id) + ' - ' + str(self.product_id) + '  : ' + self.cmt

class bill(models.Model):
	Member_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	total = models.FloatField()
	order_date = models.DateField()
	def __str__ (self):
		return str(self.id)  + ' : ' + str(self.Member_id) + ' - ' + str(self.total) + '  : ' + str(self.order_date)

class shipping(models.Model):
	bill_fk =models.ForeignKey(bill, on_delete=models.CASCADE)
	Employee_fk = models.ForeignKey(Employee, on_delete=models.CASCADE)
	Address_fk =models.ForeignKey(Address, on_delete=models.CASCADE)
	status = models.CharField(max_length=100 , default="processing")
	def __str__(self):
		return str(self.bill_fk) + '--||||--' + str(self.Address_fk)