from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import logging

from django.contrib.auth.models import User
from .forms import EditUserProfile
from apps.card_profile.models import Card


logger =logging.getLogger('novacard_info')


@login_required
def dashboard(request):
    logger.info(f"{request.user} - access dashboard page")
    cards = Card.objects.filter(created_by=request.user.id)
   
    return render(request, 'user_profile/dashboard.html', {'cards': cards, "user": request.user.id})


@login_required
def view_userprofile(request):
    logger.info(f"{request.user} - access view profile page")
    user_profile = get_object_or_404(User, username=request.user.username)
    return render(request, 'user_profile/view_profile.html', {'user_profile': user_profile})


@login_required
def edit_userprofile(request):
    logger.info(f"{request.user} - access edit profile page")
    user_profile = get_object_or_404(User, username=request.user.username)

    if request.method == 'POST':
        form = EditUserProfile(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            profile_change = form.save()
            logger.info(f"{request.user} - updated user profile data.")

            return redirect('view_userprofile')

    else:
        form = EditUserProfile()

    return render(request, 'user_profile/edit_profile.html', {'user_profile': user_profile})