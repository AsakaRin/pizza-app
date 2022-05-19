from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import render
from django.urls import reverse
from order.models import *

# Create your views here.


def index(request):

	context = {
		"BookItem": BookItem.objects.all(),
		"LaptopItem": LaptopItem.objects.all(),		
		"ClothesItem": ClothesItem.objects.all()
	}

	return render(request, "product/index.html", context)

def addProduct(request, type_product):

	context = {
		"type_product": type_product,
		"books": Book.objects.all(),
		"laptops": Laptop.objects.all(),
		"clothess": Clothes.objects.all()
	}

	return render(request, "product/addProduct.html", context)

def addProductToDB(request, type_product):

	if request.method == 'POST':

		if type_product == 'book':
			bookId = request.POST["book"]
			image = request.POST["image"]
			price = request.POST["price"]

			book = Book.objects.get(id=bookId)
			bookItem = BookItem(image=image, price=price, book=book)
			bookItem.save()
			messages.info(request, 'Add book successfully!')
		elif type_product == 'laptop':
			laptopId = request.POST["laptop"]
			image = request.POST["image"]
			price = request.POST["price"]

			laptop = Laptop.objects.get(id=laptopId)
			laptopItem = LaptopItem(image=image, price=price, laptop=laptop)
			laptopItem.save()
			messages.info(request, 'Add laptop successfully!')
		elif type_product == 'clothes':
			clothesId = request.POST["clothes"]
			image = request.POST["image"]
			price = request.POST["price"]

			clothes = Clothes.objects.get(id=clothesId)
			laptopItem = ClothesItem(image=image, price=price, clothes=clothes)
			laptopItem.save()
			messages.info(request, 'Add clothes successfully!')

		return HttpResponseRedirect(reverse('index'))

	else:
		return HttpResponse("Hello world, You're at the polls index.")

def updateProduct(request, type_product, item_id):

	data = None

	if type_product == 'book':
		data = BookItem.objects.get(id=item_id)
	elif type_product == 'laptop':
		data = LaptopItem.objects.get(id=item_id)
	elif type_product == 'clothes':
		data = ClothesItem.objects.get(id=item_id)

	context = {
		"type_product": type_product,
		"data": data,
		"books": Book.objects.all(),
		"laptops": Laptop.objects.all(),
		"clothess": Clothes.objects.all()
	}

	return render(request, "product/editProduct.html", context)

def updateProductToDB(request, type_product):

	if request.method == 'POST':

		if type_product == 'book':

			id = request.POST["id"]
			bookId = request.POST["book"]
			image = request.POST["image"]
			price = request.POST["price"]

			book = Book.objects.get(id=bookId)

			bookItem = BookItem.objects.get(id=id)
			bookItem.price = price
			bookItem.image = image
			bookItem.book = book
			bookItem.save()
			messages.info(request, 'Edit book successfully!')
		elif type_product == 'laptop':

			id = request.POST["id"]
			laptopId = request.POST["laptop"]
			image = request.POST["image"]
			price = request.POST["price"]

			laptop = Laptop.objects.get(id=laptopId)

			laptopItem = LaptopItem.objects.get(id=id)
			laptopItem.price = price
			laptopItem.image = image
			laptopItem.laptop = laptop
			laptopItem.save()
			messages.info(request, 'Edit laptop successfully!')
		elif type_product == 'clothes':

			id = request.POST["id"]
			clothesId = request.POST["clothes"]
			image = request.POST["image"]
			price = request.POST["price"]

			clothes = Clothes.objects.get(id=clothesId)

			clothesItem = ClothesItem.objects.get(id=id)
			clothesItem.price = price
			clothesItem.image = image
			clothesItem.clothes = clothes
			clothesItem.save()
			messages.info(request, 'Edit clothes successfully!')

		return HttpResponseRedirect(reverse('index'))

	else:
		return HttpResponse("Hello, world. You're at the polls index.")

def deletedProduct(request, type_product, item_id):


	if type_product == 'book':

		bookItem = BookItem.objects.get(id=item_id)
		bookItem.delete()
		messages.info(request, 'Delete book successfully!')

	elif type_product == 'laptop':

		laptopItem = LaptopItem.objects.get(id=item_id)
		laptopItem.delete()
		messages.info(request, 'Delete laptop successfully!')

	elif type_product == 'clothes':

		clothesItem = ClothesItem.objects.get(id=item_id)
		clothesItem.delete()
		messages.info(request, 'Delete clothes successfully!')
	
	return HttpResponseRedirect(reverse('index'))