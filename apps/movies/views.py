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


def movie_list(request):
    queryset = Movie.objects.order_by('title')
    form = MovieFilterForm(data=request.GET)


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
        queryset = filter_facets(facets, queryset, form, filters)
        if settings.DEBUG:
            import logging
            logger = logging.getLogger(__name__)
            logger.info(facets)

        paginator = Paginator(queryset, 1)
        page_number = request.GET.get('page')
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        context = {
            'form': form,
            'facets': facets,
            'object_list': page
        }
        return render(request, 'movies/movie_list.html', context=context)


def filter_facets(facets, queryset, form, filters):
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