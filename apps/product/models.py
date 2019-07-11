import os
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.urls import reverse, NoReverseMatch
from slugify import slugify
from django.utils.timezone import now as timezone_now

from utils.models import UrlMixin, CreationModificationDateMixin


def product_photo_upload_to(instance, filename):
    now = timezone_now()
    slug = instance.product.slug
    base, ext = os.path.splitext(filename)
    return f"products/{slug}/{now:%Y%m%d%H%M%S}{ext.lower()}"

@python_2_unicode_compatible
class Product(UrlMixin, CreationModificationDateMixin, models.Model):
    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name
    title = models.CharField('标题', max_length=200, unique=True)
    slug = models.SlugField('slug', max_length=200, unique=True)
    desc = models.TextField('描述', blank=True, null=True)
    price = models.DecimalField('价格', max_digits=8, decimal_places=2,
                                blank=True, null=True)

    def get_url_path(self):
        try:
            return reverse('product_detail', kwargs={'slug': self.slug})
        except NoReverseMatch:
            return ''

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Product, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)

@python_2_unicode_compatible
class ProductPhoto(CreationModificationDateMixin, models.Model):
    class Meta:
        verbose_name = '照片'
        verbose_name_plural = verbose_name

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField('照片', upload_to=product_photo_upload_to)

    def __str__(self):
        return self.photo.name