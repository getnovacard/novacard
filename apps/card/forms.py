from django import forms
from .models import Card

class EditCard(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'card_name',
            'active_profile',
        ]