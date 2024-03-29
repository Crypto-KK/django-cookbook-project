from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import CreationModificationDateMixin


TYPE_CHOICES = (
    ('searching', _("Searching")),
    ('offering', _("Offering")),
)


class Bulletin(CreationModificationDateMixin, models.Model):
    class Meta:
        verbose_name = _("Bulletin")
        verbose_name_plural = _("Bulletins")
        ordering = ("-created", "title",)

    bulletin_type = models.CharField(_("Type"),
                                     max_length=20,
                                     choices=TYPE_CHOICES)
    title = models.CharField(_("Title"),
                             max_length=255)
    description = models.TextField(_("Description"),
                                   max_length=300)
    contact_person = models.CharField(_("Contact person"),
                                      max_length=255)
    phone = models.CharField(_("Phone"),
                             max_length=50,
                             blank=True)
    email = models.EmailField(_("Email"),
                              max_length=254,
                              blank=True)
    image = models.ImageField(_("Image"),
                              max_length=255,
                              upload_to="bulletin_board/",
                              blank=True)

    def __str__(self):
        return self.title