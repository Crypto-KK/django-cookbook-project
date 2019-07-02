from django import forms
from django.conf import settings
from django.forms.renderers import TemplatesSetting
from django.utils.translation import ugettext_lazy as _

from crispy_forms import bootstrap, helper, layout

from .models import Bulletin


class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BulletinForm, self).__init__(*args, **kwargs)
        self.fields['bulletin_type'].widget = forms.RadioSelect()
        del self.fields['bulletin_type'].choices[0]

        title = layout.Field(
            'title',
            css_class='input-block-level'
        )
        desciption = layout.Field(
            "description",
            css_class="input-block-level",
            rows="3")
        main_fieldset = layout.Fieldset(
            _("Main data"),
            "bulletin_type",
            title,
            desciption)

        image = layout.Field(
            "image",
            css_class="input-block-level")
        format_html_template = """
                    {% load i18n %}
                    <p class="help-block">
                    {% trans "Available formats are JPG, GIF, and PNG." %}
                    {% trans "Minimal size is 800 × 800 px." %}
                    </p>
                    """
        format_html = layout.HTML(format_html_template)
        image_fieldset = layout.Fieldset(
            _("Image"),
            image,
            format_html,
            title=_("Image upload"),
            css_id="image_fieldset")

        contact_person = layout.Field(
            "contact_person",
            css_class="input-block-level")
        phone_field = bootstrap.PrependedText(
            "phone",
            '<i class="ion-ios-telephone"></i>',
            css_class="input-block-level")
        email_field = bootstrap.PrependedText(
            "email",
            "@",
            css_class="input-block-level",
            placeholder="contact@example.com")
        contact_info = layout.Div(
            phone_field,
            email_field,
            css_id="contact_info")
        contact_fieldset = layout.Fieldset(
            _("Contact"),
            contact_person,
            contact_info)

        submit_button = layout.Submit(
            "submit",
            _("Save"))
        actions = bootstrap.FormActions(submit_button)

        self.helper = helper.FormHelper()
        self.helper.form_action = "bulletin-change"
        self.helper.form_method = "POST"
        self.helper.layout = layout.Layout(
            main_fieldset,
            image_fieldset,
            contact_fieldset,
            actions)