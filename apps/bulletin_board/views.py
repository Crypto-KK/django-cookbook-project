from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Bulletin
from .forms import BulletinForm


class BulletinList(ListView):
    model = Bulletin


class BulletinEdit(FormView):
    template_name = 'bulletin_board/change_form.html'
    form_class = BulletinForm


class BulletinNew(FormView):
    template_name = 'bulletin_board/bulletin_form.html'
    form_class = BulletinForm