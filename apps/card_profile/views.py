from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import logging

from .models import Card
from .forms import EditProfile


logger =logging.getLogger('novacard_info')


@login_required
def view_card(request, username):
    logger.info(f"{request.user} - view profile {username}")
    user_profile = get_object_or_404(Card, username=username)

    return render(request, 'card_profile/view_profile.html', {'user_profile': user_profile})


@login_required
def edit_card(request, username):
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

    return render(request, 'card_profile/edit_profile.html', {'user_profile': user_profile, 'form': form})


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

    return render(request, 'card_profile/edit_profile.html', {'user_profile': user_profile, 'form': form})