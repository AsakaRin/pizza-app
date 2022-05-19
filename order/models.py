from django.db import models

class Account(models.Model):
	accountId = models.IntegerField()
	password = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.accountId}"

class Address(models.Model):
	location = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.location}"

class FullName(models.Model):
	firstName = models.CharField(max_length=64)
	lastName = models.CharField(max_length=64)	

	def __str__(self):
		return f"{self.firstName} - {self.lastName}"

class Customer(models.Model):
	phone = models.CharField(max_length=64)
	fullName = models.ForeignKey(FullName, on_delete=models.CASCADE)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.fullName}"

class Product(models.Model):
	itemId = models.IntegerField()
	type = models.IntegerField()

	def __str__(self):
		return f"{self.itemId}"

class Cart(models.Model):
	listItem = models.ManyToManyField(Product)
	totalPrice = models.IntegerField()

class Comment(models.Model):
	content = models.CharField(max_length=64)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Author(models.Model):
	name = models.CharField(max_length=64)
	phone = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"

class Publisher(models.Model):
	name = models.CharField(max_length=64)
	address = models.CharField(max_length=64)
	phone = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"

class Category(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"

class Book(models.Model):
	name = models.CharField(max_length=64)
	numberPage = models.CharField(max_length=64)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name}"

class BookItem(models.Model):
	price = models.CharField(max_length=64)
	image = models.CharField(max_length=64)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)

class Producer(models.Model):
	name = models.CharField(max_length=64)
	address = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"

class Types(models.Model):
	name = models.CharField(max_length=64)
	value = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"

class Laptop(models.Model):
	name = models.CharField(max_length=64)
	color = models.CharField(max_length=64)
	producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
	type = models.ForeignKey(Types, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name}"

class LaptopItem(models.Model):
	price = models.CharField(max_length=64)
	image = models.CharField(max_length=64)
	laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)

class Styles(models.Model):
	name = models.CharField(max_length=64)
	gender = models.IntegerField()

	def __str__(self):
		return f"{self.name}"

class Material(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"

class Clothes(models.Model):
	name = models.CharField(max_length=64)
	color = models.CharField(max_length=64)
	style = models.ForeignKey(Styles, on_delete=models.CASCADE)
	material = models.ForeignKey(Material, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name}"

class ClothesItem(models.Model):
	price = models.CharField(max_length=64)
	image = models.CharField(max_length=64)
	clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)

class Payment(models.Model):
	dateTransaction = models.CharField(max_length=64)
	method = models.IntegerField()

class Paypal(models.Model):
	paypalId = models.CharField(max_length=64)

class PayCast(models.Model):
	payCastId = models.CharField(max_length=64)

class Shipment(models.Model):
	costShip = models.IntegerField()
	nameOptionShip = models.CharField(max_length=64)

class Order(models.Model):
	dateOrder = models.CharField(max_length=64)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
	shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)