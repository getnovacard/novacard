from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import logging

from django.contrib.auth.models import User
from apps.card_profile.models import CardProfile
from apps.card.models import Card


logger =logging.getLogger('novacard_info')


@login_required
def dashboard(request):
    logger.info(f"{request.user} - access dashboard page")
    card_profiles = CardProfile.objects.filter(created_by=request.user.id)
    cards = Card.objects.filter(owner=request.user.id)

    return render(request, 'user_profile/dashboard.html', {'card_profiles': card_profiles, 'cards': cards, "user": request.user})


@login_required
def view_userprofile(request):
    logger.info(f"{request.user} - access view profile page")
    user_profile = get_object_or_404(User, username=request.user.username)
    return render(request, 'user_profile/view_profile.html', {'user_profile': user_profile})
