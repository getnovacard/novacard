from django.urls import path

from .views import view_card, edit_card

urlpatterns = [
    path('<int:card_id>/', view_card, name='view_card'),
    path('<int:card_id>/edit/', edit_card, name='edit_card'),
]
