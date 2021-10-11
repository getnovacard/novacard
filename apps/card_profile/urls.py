from django.urls import path

from .views import profiles_list, view_profile, edit_profile

urlpatterns = [
    path('', profiles_list, name='profiles_list'),
    path('profile/<str:username>/', view_profile, name='view_profile'),
    path('profile/<str:username>/edit/', edit_profile, name='edit_profile'),
]
