from django.urls import path

from .views import edit_card

urlpatterns = [
    path('<int:card_id>/edit/', edit_card, name='edit_card'),
]
