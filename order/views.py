from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.urls import reverse
from .models import Regular_Pizza, Sicilian_Pizza, Sub, Pasta, Salad, Dinner_Platter, Topping, Extra

# Create your views here.

CART = {}

PENDING = {}

COMPLETED = {}

def search(request):

	context = {
		"regular_pizza": Regular_Pizza.objects.all(), #objects.values_list('name', flat=True)
		"sicilian_pizza": Sicilian_Pizza.objects.all(),
		"sub": Sub.objects.all(),
		"pasta": Pasta.objects.all(),
		"salad": Salad.objects.all(),
		"dinner_platter": Dinner_Platter.objects.all(),
	}

	print(context)

	if request.method=="POST":
		searched = request.POST['searched']
		venues = []
		for value in context.values():
			venues.extend(value.filter(course__contains=searched)) 
		# venues = Regular_Pizza.objects.filter(course__contains=searched)
		print(venues)
		return render(request, "order/search.html", {'searched' : searched, 'venues':venues})

	else:
		return render(request, "order/search.html", {})

def index(request):

	context = {
		"regular_pizza": Regular_Pizza.objects.all(), #objects.values_list('name', flat=True)
		"sicilian_pizza": Sicilian_Pizza.objects.all(),
		"sub": Sub.objects.all(),
		"pasta": Pasta.objects.all(),
		"salad": Salad.objects.all(),
		"dinner_platter": Dinner_Platter.objects.all(),
	}

	return render(request, "order/index.html", context)

def home(request):

	context = {
		"regular_pizza": Regular_Pizza.objects.all(), #objects.values_list('name', flat=True)
		"sicilian_pizza": Sicilian_Pizza.objects.all(),
		"sub": Sub.objects.all(),
		"pasta": Pasta.objects.all(),
		"salad": Salad.objects.all(),
		"dinner_platter": Dinner_Platter.objects.all(),
	}

	return render(request, "order/home.html", context)

def custom(request, option, item_id):

	if option == "regular_pizza":
		try:
			item = Regular_Pizza.objects.get(id=item_id)
		except Regular_Pizza.DoesNotExist:
			raise Http404("item does not exist")

		list_toppings = Topping.objects.values_list('course', flat=True)

		context = {
			"option": option,
			"course": item.course,
			"size_small": item.size_small,
			"size_large": item.size_large,
			"number_toppings": item.toppings,
			"list_toppings": list_toppings,
		}

		return render(request, "order/order.html", context)

	if option == "sicilian_pizza":
		try: 
			item = Sicilian_Pizza.objects.get(id=item_id)
		except Sicilian_Pizza.DoesNotExist:
			raise Http404("item does not exist")

		list_toppings = Topping.objects.values_list('course', flat=True)

		context = {
			"option": option,
			"course": item.course,
			"size_small": item.size_small,
			"size_large": item.size_large,
			"number_toppings": item.toppings,
			"list_toppings": list_toppings,
		}

		return render(request, "order/order.html", context)

	if option == "sub":
		try: 
			item = Sub.objects.get(id=item_id)
		except Sub.DoesNotExist:
			raise Http404("item does not exist")

		list_extras = item.extras.all()

		lst = []
		for i in range(len(list_extras)):
			lst.append(str(list_extras[i]))

		context = {
			"option": option,
			"course": item.course,
			"size_small": item.size_small,
			"size_large": item.size_large,
			"list_extras": lst,
		}

		return render(request, "order/order.html", context)

	if option == "pasta":
		try:
			item = Pasta.objects.get(id=item_id)
		except Pasta.DoesNotExist:
			raise Http404("item does not exist")

		context = {
			"option": option,
			"course": item.course,
			"price": item.price,
		}

		return render(request, "order/order.html", context)

	if option == "salad":
		try:
			item = Salad.objects.get(id=item_id)
		except Salad.DoesNotExist:
			raise Http404("item does not exist")

		context = {
			"option": option,
			"course": item.course,
			"price": item.price,
		}

		return render(request, "order/order.html", context)

	if option == "dinner_platter":
		try:
			item = Dinner_Platter.objects.get(id=item_id)
		except Dinner_Platter.DoesNotExist:
			raise Http404("item does not exist")

		context = {
			"option": option,
			"course": item.course,
			"size_small": item.size_small,
			"size_large": item.size_large,
		}

		return render(request, "order/order.html", context)

def cart(request):

	if not request.user.is_authenticated:
		
		return render(request, "authentication/login.html", {"message": None})

	if request.method == 'POST':

		option = request.POST["option"]

		if option == "regular_pizza":
			option = "Regular Pizza"
			course = request.POST["course"]
			size = request.POST["type"]
			number_toppings = int(request.POST["number_toppings"])
			toppings = request.POST.getlist("topping")
			qty = request.POST["qty"]
			price = request.POST["price"]

			mess = "toppings("

			for i in range(len(toppings)):
				if i == len(toppings) - 1:
					mess = mess + toppings[i] +")"
				else:
					mess = mess + toppings[i] + ", "

			note = option.title() + " - " + course.title() + " - "  + size.title() + " - " + mess.title() + " - " + "Qty(" + qty +")" + " - " + "Price($" + price + ")"

			if request.user.username not in CART:
				CART[request.user.username] = []

			dic = {}
			dic["note"] = note
			dic["price"] = price

			CART[request.user.username].append(dic)

			print(CART)

		if option == "sicilian_pizza":
			option = "Sicilian Pizza"
			course = request.POST["course"]
			size = request.POST["type"]
			number_toppings = int(request.POST["number_toppings"])
			toppings = request.POST.getlist("topping")
			qty = request.POST["qty"]
			price = request.POST["price"]

			mess = "items("

			for i in range(len(toppings)):
				if i == len(toppings) - 1:
					mess = mess + toppings[i] +")"
				else:
					mess = mess + toppings[i] + ", "

			note = option.title()+" - "+course.title()+" - "+size.title()+" - "+mess.title()+" - "+"Qty("+qty+")"+" - "+"Price($"+price+")"

			if request.user.username not in CART:
				CART[request.user.username] = []

			dic = {}
			dic["note"] = note
			dic["price"] = price

			CART[request.user.username].append(dic)

			print(CART)

		if option == "sub":
			option = "Subs"
			course = request.POST["course"]
			size = request.POST["type"]
			extras = request.POST.getlist("topping")
			qty = request.POST["qty"]
			price = request.POST["price"]

			if len(extras) > 0:
				mess = "extras("

				for i in range(len(extras)):
					if i == len(extras) - 1:
						mess = mess + extras[i] +")"
					else:
						mess = mess + extras[i] + ", "
			else:
				mess = "no extra"

			note = option.title()+" - "+course.title()+" - "+size.title()+" - "+mess.title()+" - "+"Qty("+qty+")"+" - "+"Price($"+price+")"

			if request.user.username not in CART:
				CART[request.user.username] = []

			dic = {}
			dic["note"] = note
			dic["price"] = price

			CART[request.user.username].append(dic)

			print(CART)

		if option == "pasta":
			option = "Pasta"
			course = request.POST["course"]
			qty = request.POST["qty"]
			price = request.POST["price"]

			note = option.title()+" - "+course.title()+" - "+"Qty("+qty+")"+" - "+"Price($"+price+")"

			if request.user.username not in CART:
				CART[request.user.username] = []

			dic = {}
			dic["note"] = note
			dic["price"] = price

			CART[request.user.username].append(dic)

			print(CART)

		if option == "salad":
			option = "Salads"
			course = request.POST["course"]
			qty = request.POST["qty"]
			price = request.POST["price"]

			note = option.title()+" - "+course.title()+" - "+"Qty("+qty+")"+" - "+"Price($"+price+")"

			if request.user.username not in CART:
				CART[request.user.username] = []

			dic = {}
			dic["note"] = note
			dic["price"] = price

			CART[request.user.username].append(dic)

			print(CART)

		if option == "dinner_platter":
			option = "Dinner Platter"
			course = request.POST["course"]
			size = request.POST["type"]
			qty = request.POST["qty"]
			price = request.POST["price"]

			note = option.title()+" - "+course.title()+" - Qty("+qty+")"+" - "+"Price($"+price+")"

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
		
		return render(request, "authentication/login.html", {"message": None})

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
		return HttpResponseRedirect(reverse("home"))

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

		return HttpResponseRedirect(reverse("home"))

	if request.method == "POST":

		username = request.POST["username"]
		command = request.POST["command"]

		if command == "accept":
			pass
		COMPLETED[username] = PENDING[username]
		
		PENDING.pop(username, None)

	return HttpResponseRedirect(reverse("pending"))
def location(request):
	return render(request, "order/location.html")