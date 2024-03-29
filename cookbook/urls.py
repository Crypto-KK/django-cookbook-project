
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/', include('email_messages.urls', namespace='email_messages')),

    path('quotes/', include('quotes.urls', namespace='quote')),
    path('bulletins/', include('bulletin_board.urls', namespace='bulletins')),

    path('movies/', include('movies.urls')),

    path('cv/', include('cv.urls')),
    path('search/', include('haystack.urls')),
]
