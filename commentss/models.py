from __future__ import unicode_literals

from django.db import models
from userss.models import UserProfile
from cardss.models import Cards
from django.utils import timezone

# Create your models here.


class Comment(models.Model):

    user = models.ForeignKey(
        UserProfile,
        default="",
        null=True,
        blank=True,
        related_name='user_comments')

    comment_on_card = models.ForeignKey(
        Cards,
        default="",
        null=True,
        blank=True,
        related_name='card_comments')

    comments = models.TextField(
        blank="True", null='True', verbose_name='your comment')

    count = models.IntegerField(default=0)

    comment_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
