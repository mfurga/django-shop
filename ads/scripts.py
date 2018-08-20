from django.template.defaultfilters import slugify

import datetime
import hashlib
import string
import random
import os


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
