from django.db import models

# Create your models here.

class Topping(models.Model):

	course = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.course}"

class Regular_Pizza(models.Model):

	course = models.CharField(max_length=64)
	size_small = models.CharField(max_length=64)
	size_large = models.CharField(max_length=64)
	toppings = models.IntegerField()

	def __str__(self):
		return f"{self.course} - {self.size_small} - {self.size_large}"

class Sicilian_Pizza(models.Model):

	course = models.CharField(max_length=64)
	size_small = models.CharField(max_length=64)
	size_large = models.CharField(max_length=64)
	toppings = models.IntegerField()

	def __str__(self):
		return f"{self.course} - {self.size_small} - {self.size_large}"

class Extra(models.Model):

	course = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.course}"

class Sub(models.Model):

	course = models.CharField(max_length=64)
	size_small = models.CharField(max_length=64, blank=True)
	size_large = models.CharField(max_length=64)
	extras = models.ManyToManyField(Extra, blank=True)

	def __str__(self):
		return f"{self.course} - {self.size_small} - {self.size_large}"

class Pasta(models.Model):

	course = models.CharField(max_length=64)
	price = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.course} - {self.price}"

class Salad(models.Model):

	course = models.CharField(max_length=64)
	price = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.course} - {self.price}"

class Dinner_Platter(models.Model):

	course = models.CharField(max_length=64)
	size_small = models.CharField(max_length=64)
	size_large = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.course} - {self.size_small} - {self.size_large}"