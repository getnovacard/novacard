from django.shortcuts import render, get_object_or_404, redirect
from apps.card_profile.models import CardProfile
from apps.card.models import Card
import logging

logger =logging.getLogger('novacard_info')


def display_profile_card_id(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    card_profile = get_object_or_404(CardProfile, pk=card.active_profile.id)
    card_profile_name = card_profile.card_profile_name
    return redirect(display_profile_card_profile_name, card_profile_name=card_profile_name)


def display_profile_card_profile_name(request, card_profile_name):
    card_profile = get_object_or_404(CardProfile, card_profile_name=card_profile_name)
    template_path = card_profile.template.template_path
    template = f'{template_path}/index.html'

    return render(request, template, {'card_profile': card_profile})
