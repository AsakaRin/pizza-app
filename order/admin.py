from django.contrib import admin
from django.db.models.fields.files import ImageField

# Register your models here.
from .models import *

admin.site.register(Account)
admin.site.register(Address)
admin.site.register(FullName)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(Producer)
admin.site.register(Types)
admin.site.register(Laptop)
admin.site.register(LaptopItem)
admin.site.register(Styles)
admin.site.register(Material)
admin.site.register(Clothes)
admin.site.register(ClothesItem)
admin.site.register(Payment)
admin.site.register(Paypal)
admin.site.register(PayCast)
admin.site.register(Shipment)
admin.site.register(Order)