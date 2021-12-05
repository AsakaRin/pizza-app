from django.contrib import admin
from django.db.models.fields.files import ImageField

# Register your models here.
from .models import Regular_Pizza, Sicilian_Pizza, Sub, Pasta, Salad, Dinner_Platter, Topping, Extra

admin.site.register(Dinner_Platter)
admin.site.register(Salad)
admin.site.register(Pasta)
admin.site.register(Extra)
admin.site.register(Sub)
admin.site.register(Topping)
admin.site.register(Sicilian_Pizza)
admin.site.register(Regular_Pizza)