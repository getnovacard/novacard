from django.contrib.auth.models import User
from django.db import models

from apps.card_profile.models import CardProfile


class CardModel(models.Model):
    card_model = models.CharField(max_length=255, blank=False, null=False)

    created_by = models.ForeignKey(User, related_name='card_model', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    changed_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.card_model}'
 

class Card(models.Model):

    STANDARD = 'standard'
    LOGO_AND_NAME = 'logo_and_name'
    CUSTOM_DESIGN = 'custom_design'

    CHOICES_DESIGN = (
        (STANDARD, 'standard'),
        (LOGO_AND_NAME, 'logo_and_name'),
        (CUSTOM_DESIGN, 'custom_design'),
    )

    card_name = models.CharField(max_length=255, blank=False, null=False)
    card_model = models.ForeignKey(CardModel, related_name='card', on_delete=models.CASCADE)
    card_design = models.CharField(max_length=255, blank=False, null=False, choices=CHOICES_DESIGN)
    active_profile = models.ForeignKey(CardProfile, related_name='card_active_profile', on_delete=models.CASCADE, blank=True, null=True)
    
    owner = models.ForeignKey(User, related_name='card_owner', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='card', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    changed_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.card_name


class CardSubscription(models.Model):
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    card = models.OneToOneField(Card, related_name='card_subscription', on_delete=models.CASCADE)
    
    created_by = models.ForeignKey(User, related_name='card_subscription', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    changed_at = models.DateTimeField(auto_now=True, blank=True, null=True)  
    
    def __str__(self):
        return f'{self.card}'