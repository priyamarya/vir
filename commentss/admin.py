from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'comment_on_card']
admin.site.register(Comment, CommentAdmin)
