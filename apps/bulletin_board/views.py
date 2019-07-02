from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, UpdateView
from .models import Bulletin
from .forms import BulletinForm


class BulletinList(ListView):
    model = Bulletin
    context_object_name = 'bullet'


class BulletinEdit(UpdateView):
    model = Bulletin
    template_name = 'bulletin_board/bulletin_update.html'
    form_class = BulletinForm

    def get_success_url(self):
        return reverse_lazy('bulletins:bulletin-list')
    
    def form_valid(self, form):
        form.save()
        return super(BulletinEdit, self).form_valid(form)


class BulletinNew(FormView):
    template_name = 'bulletin_board/change_form.html'
    form_class = BulletinForm

    def get_success_url(self):
        return reverse_lazy('bulletins:bulletin-list')

    def form_valid(self, form):
        form.save()
        return super(BulletinNew, self).form_valid(form)

