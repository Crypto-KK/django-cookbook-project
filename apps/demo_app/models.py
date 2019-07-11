from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.models import (CreationModificationDateMixin,
                          MetaTagsMixin,
                          UrlMixin,
                          object_relation_mixin_factory)
from utils.fields import (
    MultilingualCharField,
    MultilingualTextField
)


FavoriteObjectMixin = object_relation_mixin_factory(is_required=True)
OwnerMixin = object_relation_mixin_factory(
    prefix='owner',
    prefix_verbose=_('Owner'),
    is_required=True,
    add_related_name=True,
    limit_content_type_choices_to={
        'model__in': ('user', 'institution')
    }
)

class Like(FavoriteObjectMixin, OwnerMixin):
    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return _(f"{self.owner_content_object} "
                 f"likes {self.content_object}")


class Category(models.Model):
    title = models.CharField('Title', max_length=200)

    def __str__(self):
        return self.title


class Idea(UrlMixin, CreationModificationDateMixin, MetaTagsMixin):
    class Meta:
        verbose_name = 'Idea'
        verbose_name_plural = 'Ideas'

    title = models.CharField('Title', max_length=200)
    description = models.CharField('Description', max_length=200, blank=True)
    content = models.TextField('Content')

    categories = models.ManyToManyField(Category,
                                        verbose_name='Category',
                                        blank=True,
                                        related_name='ideas')


    def __str__(self):
        return self.title

    def get_url_path(self):
        return reverse('idea-detail', kwargs={
            'pk': str(self.pk)
        })


