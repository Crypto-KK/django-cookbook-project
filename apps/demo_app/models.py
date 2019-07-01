from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.models import (CreationModificationDateMixin,
                          MetaTagsMixin,
                          UrlMixin)

class Idea(UrlMixin, CreationModificationDateMixin, MetaTagsMixin):
    class Meta:
        verbose_name = _('Idea')
        verbose_name_plural = _('Ideas')


    title = models.CharField(_('Title'), max_length=200)
    content = models.TextField(_('Content'))

    def __str__(self):
        return self.title

    def get_url_path(self):
        return reverse('idea-detail', kwargs={
            'pk': str(self.pk)
        })


