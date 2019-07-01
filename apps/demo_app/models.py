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
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')

    def __str__(self):
        return _(f"{self.owner_content_object} "
                 f"likes {self.content_object}")



class Idea(UrlMixin, CreationModificationDateMixin, MetaTagsMixin):
    class Meta:
        verbose_name = _('Idea')
        verbose_name_plural = _('Ideas')


    # title = models.CharField(_('Title'), max_length=200)
    # content = models.TextField(_('Content'))
    title = MultilingualCharField(_('Title'), max_length=200)
    description = MultilingualTextField(_('Description'), blank=True)
    content = MultilingualTextField(_('Content'))

    def __str__(self):
        return self.title

    def get_url_path(self):
        return reverse('idea-detail', kwargs={
            'pk': str(self.pk)
        })


