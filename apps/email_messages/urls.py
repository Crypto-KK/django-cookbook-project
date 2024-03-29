from django.urls import path

from .views import message_sent, message_to_user

app_name = 'email_messages'

urlpatterns = [
    path('', message_to_user, name='message_to_user'),
    path('sent/', message_sent, name='message_sent')
]