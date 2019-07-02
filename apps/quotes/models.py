import os

from django.db import models
from django.utils.timezone import now as timezone_now

def upload_to(instance, filename):
    now = timezone_now()
    base, ext = os.path.splitext(filename)
    ext = ext.lower()
    return f'quotes/{now:%Y/%m/%Y%m%d%H%M%S}{ext}'


class Quote(models.Model):
    class Meta:
        verbose_name = 'quote'
        verbose_name_plural = verbose_name

    author = models.CharField('author', max_length=200)
    quote = models.TextField('quote')
    picture = models.ImageField('picture', upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.quote


