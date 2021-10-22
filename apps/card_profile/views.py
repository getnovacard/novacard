from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import logging

from .models import Card
from .forms import EditProfile


logger =logging.getLogger('novacard_info')


@login_required
def view_card(request, card_id):
    logger.info(f"{request.user} - view card {card_id}")
    card_profile = get_object_or_404(Card, pk=card_id)
    if request.user.id == card_profile.created_by.id:
        return render(request, 'card_profile/view_card.html', {'card_profile': card_profile})
    else:
        return render(request, 'core/message.html', {'message': 'You are not authorized to view this information'})


@login_required
def edit_card(request, card_id):
    card_profile = get_object_or_404(Card, pk=card_id)

    if request.user.id == card_profile.created_by.id:
        if request.method == 'POST':
            form = EditProfile(request.POST, request.FILES, instance=card_profile)

            if form.is_valid():
                profile_change = form.save(commit=False)
                profile_change.created_by = request.user
                profile_change.save()
                logger.info(f"{request.user} - updated card data.")

                return redirect('view_card', card_id=card_id)

        else:
            form = EditProfile()
            logger.info(f"{request.user} - edit card {card_profile.id}")

        return render(request, 'card_profile/edit_card.html', {'card_profile': card_profile, 'form': form})
    
    else:
        return render(request, 'core/message.html', {'message': 'You are not authorized to view this information'})


@login_required
def create_card(request, username):
    user_profile = get_object_or_404(Card, username=username)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            profile_change = form.save(commit=False)
            profile_change.created_by = request.user
            profile_change.save()
            logger.info(f"{request.user} - updated profile data.")

            return redirect('view_profile', username=user_profile.username)

    else:
        form = EditProfile()
        logger.info(f"{request.user} - edit profile {username}")

    return render(request, 'card_profile/edit_card.html', {'user_profile': user_profile, 'form': form})