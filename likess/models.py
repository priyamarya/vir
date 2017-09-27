from __future__ import unicode_literals

from django.db import models
from cardss.models import Cards
from userss.models import UserProfile
from django.utils import timezone

# Create your models her


class CardLikes(models.Model):
    user = models.ForeignKey(
        UserProfile,
        default="",
        null=True,
        related_name='user_likes',
        blank=True)

    like_on_card = models.ForeignKey(
        Cards,
        default="",
        null=True,
        blank=True,
        related_name='card_likes')

    like = models.IntegerField(default=0)

    like_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = 'Like'
