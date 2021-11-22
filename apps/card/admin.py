from django.contrib import admin

from .models import CardModel, CardSubscription, Card

admin.site.register(CardModel)
admin.site.register(CardSubscription)
admin.site.register(Card)
