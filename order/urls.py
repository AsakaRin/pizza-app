from django.urls import path

from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("<str:option>/<int:item_id>", views.custom, name="custom"),
	path("cart", views.cart, name="cart"),
	path("mycart", views.mycart, name="mycart"),
	path("pending", views.pending, name="pending"),
	path("processing", views.processing, name="processing"),
	path("completed", views.completed, name="completed"),
	path("confirm", views.confirm, name="confirm"),
]