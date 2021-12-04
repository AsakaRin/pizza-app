from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def index(request):

	if not request.user.is_authenticated:
		
		return render(request, "authentication/login.html", {"message": None})

	context = {
		"user": request.user
		
	}	

	return HttpResponseRedirect(reverse("home"))

def login_view(request):

	if request.method == 'POST':

		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "authentication/login.html", {"message": "Invalid credentials."})

	else:

		return render(request, "authentication/login.html")

def register_view(request):

	if request.method == 'POST':

		username = request.POST["username"]
		password = request.POST["password"]
		email = request.POST["email"]
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]

		# register for user
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.last_name = last_name
		user.save()

		# auto login after register
		user = authenticate(request, username=username, password=password)
		login(request, user)
		return HttpResponseRedirect(reverse("index"))

	else:

		return render(request, "authentication/register.html")

def logout_view(request):

	if not request.user.is_authenticated:
		return render(request, "authentication/login.html")

	logout(request)
	return HttpResponseRedirect(reverse("login"))



