from django.contrib import admin
from .models import Cards
from .forms import CardsForm
# Register your models here.


class CardsAdmin(admin.ModelAdmin):
	form = CardsForm
	list_display = ['__str__', 'user']

admin.site.register(Cards, CardsAdmin)
