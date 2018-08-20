from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.conf import settings
from django.db import models

from .scripts import get_image_filename, slug_generator

CATEGORIES = (
    (1, _('Automotive')),
    (2, _('Electronics')),
    (3, _('House and Garden')),
    (4, _('Immovables')),
    (5, _('Books')),
    (6, _('Games')),
    (7, _('Sport')),
    (8, _('Farming')),
    (9, _('Pets')),
    (10, _('Movies & Music')),
)

CONDITIONS = (
    (0, _('Usage')),
    (1, _('New'))
)


class Image(models.Model):
    image = models.ImageField(upload_to=get_image_filename)
    prime = models.BooleanField(default=False)

    class Meta:
        ordering = ['-prime']

    def get_absolute_url(self):
        return self.image.url


class Ad(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    category = models.IntegerField(choices=CATEGORIES)
    description = models.TextField()
    condition = models.IntegerField(choices=CONDITIONS)
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    has_image = models.BooleanField(default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.title


def pre_save_ad(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance)

pre_save.connect(pre_save_ad, sender=Ad)
