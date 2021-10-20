from django.urls import path

from .views import view_userprofile, edit_userprofile

urlpatterns = [
    path('', view_userprofile, name='view_userprofile'),
    path('edit/', edit_userprofile, name='edit_userprofile'),    
]
