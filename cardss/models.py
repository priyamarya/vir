from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from userss.models import UserProfile
from django.contrib.auth.models import User

from froala_editor.fields import FroalaField
# Create your models here.

TYPE_CHOICES = (("public", "public"), ("private", "private"))


class Cards(models.Model):
    """Creating a model."""

    user = models.ForeignKey(
        UserProfile,
        default="",
        null=True,
        blank=True)

    name = models.CharField(
        max_length=200,
        blank=False,
        null=False)

    image = models.ImageField(
        upload_to='Cards',
        blank=False,
        null=False,
        verbose_name="Banner Image for your blog")

    desc = FroalaField(null=True,blank=True)

    v_type = models.CharField(max_length=125, choices=TYPE_CHOICES, default="public")

    likes = models.IntegerField(default=0)

    # liked_by = models.ForeignKey(
    #     User,
    #     default="",
    #     related_name='likedby',
    #     null=True,
    #     blank=True)

    upload_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="time")

    def __str__(self):
        """Show on admin."""
        return self.name

    class Meta:
        """This will show on admin main page."""

        verbose_name = 'Cards'
        verbose_name_plural = "Cards"

