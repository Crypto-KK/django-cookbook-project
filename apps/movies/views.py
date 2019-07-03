from django.conf import settings

from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import (
    EmptyPage,
    PageNotAnInteger,
    Paginator
)

from .models import Genre, Director, Actor, Movie, RATING_CHOICES
from .forms import MovieFilterForm



class MovieListView(View):
    form_class = MovieFilterForm
    template_name = 'movies/movie_list.html'
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        form = self.form_class(data=request.GET)
        queryset, facets = self.get_queryset_and_facets(form)
        page = get_paginate(request, queryset=queryset)
        context = {
            'form': form,
            'facets': facets,
            'object_list': page
        }
        return render(request, template_name=self.template_name, context=context)


    def get_queryset_and_facets(self, form):
        queryset = Movie.objects.order_by('title')
        facets = {
            'selected': {},
            'categories': {
                'genres': Genre.objects.all(),
                'directors': Director.objects.all(),
                'actors': Actor.objects.all(),
                'ratings': RATING_CHOICES
            }
        }
        if form.is_valid():
            filters = (
                ("genre", "genres",),
                ("director", "directors",),
                ("actor", "actors",),
                ("rating", "rating",),
            )
            queryset = self.filter_facets(facets, queryset, form, filters)
        return queryset, facets

    def filter_facets(self, facets, queryset, form, filters):
        for facet, key in filters:
            value = form.cleaned_data[facet]
            if value:
                selected_value = value
                if facet == 'rating':
                    rating = int(value)
                    selected_value = (
                        rating, dict(RATING_CHOICES)[rating]
                    )
                    filter_args = {
                        f"{key}__gte": rating,
                        f"{key}__lt": rating + 1
                    }
                else:
                    filter_args = {
                        key: value
                    }
                facets['selected'][facet] = selected_value
                queryset = queryset.filter(**filter_args).distinct()

        return queryset




def get_paginate(request, queryset):
    """:return object list that paginate by queryset"""
    paginator = Paginator(queryset, 1)
    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(settings.MAX_PAGE_SIZE)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page