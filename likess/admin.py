from django.contrib import admin
from .models import CardLikes
# Register your models here.


class CardLikesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'like_on_card']

admin.site.register(CardLikes, CardLikesAdmin)
