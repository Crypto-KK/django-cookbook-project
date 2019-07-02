
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/', include('email_messages.urls', namespace='email_messages')),

    path('quotes/', include('quotes.urls', namespace='quote'))
]
