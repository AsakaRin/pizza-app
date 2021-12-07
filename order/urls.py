from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("menu", views.menu, name="menu"), 
	path("<str:option>/<int:item_id>", views.custom, name="custom"),
	path("cart", views.cart, name="cart"),
	path("mycart", views.mycart, name="mycart"),
	path("pending", views.pending, name="pending"),
	path("processing", views.processing, name="processing"),
	path("completed", views.completed, name="completed"),
	path("confirm", views.confirm, name="confirm"),
	path("search", views.search, name="search"),
	path("location", views.location, name="location"),
	path("contact",views.contact,name="contact")
]