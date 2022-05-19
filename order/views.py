from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate
from django.http.response import Http404
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.core import serializers

# Create your views here.

CART = {}

PENDING = {}

COMPLETED = {}

def index(request):

	context = {
		"BookItem": BookItem.objects.all(),
		"LaptopItem": LaptopItem.objects.all(),		
		"ClothesItem": ClothesItem.objects.all()
	}

	return render(request, "order/index.html", context)

def menu(request):

	return render(request, "order/menu.html")

def getmenu(request):

	if request.is_ajax and request.method == "GET":

		key = request.GET.get("key", None)		

		context = {
			"BookItem": BookItem.objects.all(),
			"LaptopItem": LaptopItem.objects.all(),		
			"ClothesItem": ClothesItem.objects.all()
		}	

		# convert queryset to json
		data = {}
		data["BookItem"] = []
		for item in context["BookItem"]:

			if key != '' and key != None:
				if key not in item.book.name:
					continue
			obj = {
				'id': item.id,
				'image': item.image,
				'name': item.book.name,
				'price': item.price,
				'type': 'BookItem'
			}
			data['BookItem'].append(obj)

		data["LaptopItem"] = []
		for item in context["LaptopItem"]:

			if key != '' and key != None:
				if key not in item.laptop.name:
					continue

			obj = {
				'id': item.id,
				'image': item.image,
				'name': item.laptop.name,
				'price': item.price,
				'type': 'LaptopItem'
			}
			data['LaptopItem'].append(obj)

		data["ClothesItem"] = []
		for item in context["ClothesItem"]:

			if key != '' and key != None:
				if key not in item.clothes.name:
					continue

			obj = {
				'id': item.id,
				'image': item.image,
				'name': item.clothes.name,
				'price': item.price,
				'type': 'ClothesItem'
			}
			data['ClothesItem'].append(obj)		

		return JsonResponse(data, status = 200)      

	return JsonResponse({}, status = 400)


def custom(request, option, item_id):

	if option == "bookItem":
		try:
			item = BookItem.objects.get(id=item_id)
		except BookItem.DoesNotExist:
			raise Http404("item does not exist")

		context = {
			'id': item.id,
			'image': item.image,
			'name': item.book.name,
			'price': item.price,
			'option': option
		}

		return render(request, "order/order.html", context)

	if option == "laptopItem":
		try:
			item = LaptopItem.objects.get(id=item_id)
		except LaptopItem.DoesNotExist:
			raise Http404("item does not exist")

		context = {
			'id': item.id,
			'image': item.image,
			'name': item.laptop.name,
			'price': item.price,
			'option': option
		}

		return render(request, "order/order.html", context)

	if option == "clothesItem":
		try:
			item = ClothesItem.objects.get(id=item_id)
		except ClothesItem.DoesNotExist:
			raise Http404("item does not exist")

		context = {
			'id': item.id,
			'image': item.image,
			'name': item.clothes.name,
			'price': item.price,
			'option': option
		}

		return render(request, "order/order.html", context)

def cart(request):

	if not request.user.is_authenticated:
		
		return HttpResponseRedirect(reverse("login"))

	if request.method == 'POST':

		option = request.POST["option"]

		if option == "bookItem":
			option = "bookItem"
			name = request.POST["name"]					
			qty = request.POST["qty"]
			price = request.POST["price"]

			note = "Book: " + name.title() + " - " + "Qty(" + qty +")" + " - " + "Price($" + price + ")"

			if request.user.username not in CART:
				CART[request.user.username] = []

			dic = {}
			dic["note"] = note
			dic["price"] = price

			CART[request.user.username].append(dic)

			print(CART)

		if option == "laptopItem":
			option = "laptopItem"
			name = request.POST["name"]					
			qty = request.POST["qty"]
			price = request.POST["price"]

			note = "Laptop: " + name.title() + " - " + "Qty(" + qty +")" + " - " + "Price($" + price + ")"

			if request.user.username not in CART:
				CART[request.user.username] = []

			dic = {}
			dic["note"] = note
			dic["price"] = price

			CART[request.user.username].append(dic)

			print(CART)

		if option == "clothesItem":
			option = "clothesItem"
			name = request.POST["name"]					
			qty = request.POST["qty"]
			price = request.POST["price"]

			note = "Clothes: " + name.title() + " - " + "Qty(" + qty +")" + " - " + "Price($" + price + ")"

			if request.user.username not in CART:
				CART[request.user.username] = []

			dic = {}
			dic["note"] = note
			dic["price"] = price

			CART[request.user.username].append(dic)

			print(CART)

		context = {
			"cart": CART[request.user.username],
		}

		return HttpResponseRedirect(reverse("mycart"))

	else:
		
		return HttpResponseRedirect(reverse("mycart"))

def mycart(request):

	if not request.user.is_authenticated:
		
		return HttpResponseRedirect(reverse("login"))

	if request.user.username not in CART:
		return render(request, "order/cart.html")

	context = {
		"cart": CART[request.user.username],
	}

	return render(request, "order/cart.html", context)

def processing(request):

	if not request.user.is_authenticated:
		
		return render(request, "authentication/login.html", {"message": None})

	if request.user.username not in CART:
		return HttpResponseRedirect(reverse("menu"))

	PENDING[request.user.username] = CART[request.user.username]
	CART.pop(request.user.username, None)

	return HttpResponseRedirect(reverse("pending"))

def pending(request):

	if not request.user.is_authenticated:
		
		return render(request, "authentication/login.html", {"message": None})

	# if not superuser
	if not request.user.is_superuser:

		if request.user.username not in PENDING:
			return render(request, "order/pending.html")

		context = {
			"pending": PENDING[request.user.username],
		}

		return render(request, "order/pending.html", context)

	# if superuser
	else:

		costs = {}

		for username in PENDING:
			count = 0
			for element in PENDING[username]:
				print(element)
				count += float(element["price"])
			costs[username] = count
		print(costs)

		context = {
			"pending": PENDING,
			"costs": costs,
		}

		return render(request, "order/pending.html", context)

def completed(request):

	if not request.user.is_authenticated:
		
		return render(request, "authentication/login.html", {"message": None})

	# if not superuser
	if not request.user.is_superuser:

		if request.user.username not in COMPLETED:
			return render(request, "order/completed.html")

		context = {
			"completed": COMPLETED[request.user.username],
		}

		return render(request, "order/completed.html", context)

	# if superuser
	else:

		costs = {}

		for username in COMPLETED:
			count = 0
			for element in COMPLETED[username]:
				count += float(element["price"])
			costs[username] = count

		context = {
			"completed": COMPLETED,
			"costs": costs,
		}

		return render(request, "order/completed.html", context)

def confirm(request):

	if not request.user.is_authenticated:
		
		return render(request, "authentication/login.html", {"message": None})

	if not request.user.is_superuser:

		return HttpResponseRedirect(reverse("menu"))

	if request.method == "POST":

		username = request.POST["username"]
		command = request.POST["command"]

		if command == "accept":
			COMPLETED[username] = PENDING[username]			
			PENDING.pop(username, None)
		else:
			PENDING.pop(username, None)

	return HttpResponseRedirect(reverse("pending"))

def location(request):
	return render(request, "order/location.html")

def contact(request):
	if request.method=="POST":
		message_name = request.POST['message-name']
		message_email= request.POST['message-email']
		message =request.POST['message']
		send_mail
		send_mail(
			"Pinochio's Pizza",
			'Thanks for your response!',
			'phanthin1912@gmail.com',
			[message_email],
		)
		
		return render(request, "order/contact.html", {'message_name': message_name})		

	else:
		return render(request, "order/contact.html", {})		
