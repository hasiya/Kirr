from django.db import models
from django.conf import settings

from django_hosts.resolvers import reverse

from .utils import code_generator, create_shortcode
from .validators import validate_url

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcode(self, items=None):
        print(items)
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New Codes Made: {i}".format(i=new_codes)


class KirrURL(models.Model):
    """docstring for KirrURL"""
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = KirrURLManager()

    def save(self, *args, **kwargs):
        if not self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)

        if not "http" in self.url:
            self.url = "http://" + self.url

        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme="http", port='8000')
        return url_path
