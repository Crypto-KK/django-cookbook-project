from django.shortcuts import render, redirect

from .forms import QuoteForm

def add_quote(request):
    form = QuoteForm()
    if request.method == 'POST':
        form = QuoteForm(
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect('quote:add_quote')
    else:
        return render(request, 'quotes/add_quote.html', {
            'form': form
        })

