from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("<str:type_product>/addProduct", views.addProduct, name="addProduct"),
	path("<str:type_product>/addProductToDB", views.addProductToDB, name="addProductToDB"),
	path("<str:type_product>/updateProduct/<int:item_id>", views.updateProduct, name="updateProduct"),
	path("<str:type_product>/updateProduct/updateProductToDB", views.updateProductToDB, name="updateProductToDB"),
	path("<str:type_product>/deletedProduct/<int:item_id>", views.deletedProduct, name="deletedProduct")
]