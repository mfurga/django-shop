from django.template.defaultfilters import slugify

import datetime
import hashlib
import string
import random
import os


class RequestGETParse(object):

    # Constructor
    def __init__(self, ads):
        self.ads = ads

    # Filtering by query search
    def query(self, q):
        self.ads = self.ads.filter(title__contains=q)

    # Filtering by location
    def location(self, loc):
        self.ads = self.ads.filter(location__contains=loc)

    # Filtering by category
    def category(self, cat):
        self.ads = self.ads.filter(category=cat)

    # Filtering by condition
    def condition(self, cond):
        self.ads = self.ads.filter(condition=cond)

    # Filtering by min price
    def price_from(self, pmin):
        self.ads = self.ads.filter(price__gte=pmin)

    # Filtering by max price
    def price_to(self, pmax):
        self.ads = self.ads.filter(price__lte=pmax)

    # Filtering by image
    def image_only(self, bool):
        self.ads = self.ads.filter(has_image=True)

    # Sorting by time
    def sort_time(self, sort_type):
        if sort_type == 'up':
            self.ads = self.ads.order_by('pub_date')
        elif sort_type == 'down':
            self.ads = self.ads.order_by('-pub_date')

    # Sorting by price
    def sort_price(self, sort_type):
        if sort_type == 'up':
            self.ads = self.ads.order_by('price')
        elif sort_type == 'down':
            self.ads = self.ads.order_by('-price')

    def get_objects(self):
        return self.ads


def random_string(length=4):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def slug_generator(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    Ad = instance.__class__
    exists = Ad.objects.filter(slug=slug).exists()
    if exists:
        new_slug = '{slug}-{random}'.format(slug=slug, random=random_string())
        return slug_generator(instance, new_slug=new_slug)
    return slug


def get_image_filename(instance, file):
    filename, extension = os.path.splitext(file)
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
    name = hashlib.md5((filename + date).encode('utf-8')).hexdigest()
    return 'images/{name}{extension}'.format(name=name, extension=extension)
