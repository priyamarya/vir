from django.contrib import admin
from .models import UserProfile, UserProfileInfo

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    # class Meta:
    #     model = UserProfile
    list_display = ['__str__', 'email', 'joining_date']


class UserProfileInfoAdmin(admin.ModelAdmin):
    # class Meta:
    #     model = UserProfile
    list_display = ['__str__', 'gender']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
