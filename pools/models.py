from django.db import models

# Create your models here.
class Members(models.Model):
	id = models.AutoField(primary_key=True)
	userName = models.CharField(max_length = 100)
	passWord = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)

	def __str__(self):
		return self.userName + ' : ' + self.name

class Products(models.Model):
	product_id = models.AutoField(primary_key=True)
	product_name = models.CharField(max_length=100)
	product_price = models.FloatField()
	product_quantity = models.IntegerField()
	product_cmt = models.CharField(max_length=1000)
	def __str__(self):
		return str(self.product_id) + ': ' + self.product_name + ' - ' + str(self.product_price)


class order_products(models.Model):
	Member_id = models.IntegerField()
	product_id = models.IntegerField()
	product_price = models.FloatField()
	total = models.IntegerField()
	order_date = models.DateField()
	order_status = models.IntegerField()
	
	def __str__(self):
		return 'order  ' + 'id member'  + str(self.Member_id) + '- id product :  ' + str(self.product_id)
class product_cmt(models.Model):
	Member_id = models.IntegerField()
	product_id = models.IntegerField()
	cmt = models.CharField(max_length = 2000)
	
	def __str__ (self):
		return str(self.Member_id) + ' - ' + str(self.product_id) + '  : ' + self.cmt

class bill(models.Model):
	Member_id = models.IntegerField()
	total = models.FloatField()
	order_date = models.DateField()

	def __str__ (self):
		return str(self.id)  + ' : ' + str(self.Member_id) + ' - ' + str(self.total) + '  : ' + str(self.order_date)