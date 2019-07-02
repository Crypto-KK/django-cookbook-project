from django.urls import path, reverse_lazy, reverse

from .views import (
    BulletinList,
    BulletinEdit,
    BulletinNew
)

app_name = 'bulletins'

# edit_view = BulletinEdit.as_view(
#     success_url=reverse_lazy('bulletin-list')
# )


urlpatterns = [
    path('', BulletinList.as_view(), name='bulletin-list'),
    path('<int:pk>/edit/', BulletinEdit.as_view(), name='bulletin-edit'),
    path('new/', BulletinNew.as_view(), name='bulletin-new'),
]