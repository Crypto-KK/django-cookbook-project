from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class MessageForm(forms.Form):
    recipient = forms.ModelChoiceField(
        label='recipient',
        queryset=User.objects.all(),
        required=True
    )
    message = forms.CharField(
        label='message',
        widget=forms.Textarea,
        required=True
    )


    def __init__(self, request, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['recipient'].queryset.exclude(
            pk=request.user.pk
        )

    def save(self):
        cleaned_data = self.cleaned_data

