from django.urls import path

from .views import view_card_profile, edit_card_profile, delete_card_profile, create_card_profile, download_vcard

urlpatterns = [
    path('<int:card_profile_id>/', view_card_profile, name='view_card_profile'),
    path('<int:card_profile_id>/edit/', edit_card_profile, name='edit_card_profile'),
    path('<int:card_profile_id>/delete/', delete_card_profile, name='delete_card_profile'),
    path('create/', create_card_profile, name='create_card_profile'),
    path('<int:card_profile_id>/download_vcard/',download_vcard , name='download_vcard'),
]
