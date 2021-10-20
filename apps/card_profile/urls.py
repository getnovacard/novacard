from django.urls import path

from .views import view_card, edit_card

urlpatterns = [
    path('<str:username>/', view_card, name='view_card'),
    path('<str:username>/edit/', edit_card, name='edit_card'),
]
