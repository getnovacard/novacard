from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging

from .models import Card
from .forms import EditCard
from apps.card_profile.models import CardProfile

logger =logging.getLogger('novacard_info')

@login_required
def edit_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    card_profiles = CardProfile.objects.filter(created_by=request.user)

    if request.user.id == card.owner.id:
        if request.method == 'POST':
            form = EditCard(request.POST, instance=card)

            if form.is_valid():
                form.save()
                logger.info(f"{request.user} - updated card data.")

                return redirect('dashboard')

        else:
            form = EditCard()
            logger.info(f"{request.user} - edit card {card.id}")

        return render(request, 'card/edit_card.html', {'card': card, 'form': form, 'card_profiles': card_profiles})
    
    else:
        return render(request, 'core/message.html', {'message': 'You are not authorized to view this information'})