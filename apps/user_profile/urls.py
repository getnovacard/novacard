from django.urls import path

from .views import view_userprofile

urlpatterns = [
    path('', view_userprofile, name='view_userprofile'),
]
