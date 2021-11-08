from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging

from .models import CardProfile
from .forms import EditProfile


logger =logging.getLogger('novacard_info')


@login_required
def view_card_profile(request, card_profile_id):
    logger.info(f"{request.user} - view card {card_profile_id}")
    card_profile = get_object_or_404(CardProfile, pk=card_profile_id)
    if request.user.id == card_profile.created_by.id:
        return render(request, 'card_profile/view_card_profile.html', {'card_profile': card_profile})
    else:
        return render(request, 'core/message.html', {'message': 'You are not authorized to view this information'})


@login_required
def edit_card_profile(request, card_profile_id):
    card_profile = get_object_or_404(CardProfile, pk=card_profile_id)

    if request.user.id == card_profile.created_by.id:
        if request.method == 'POST':
            form = EditProfile(request.POST, request.FILES, instance=card_profile)

            if form.is_valid():
                profile_change = form.save(commit=False)
                profile_change.created_by = request.user
                profile_change.save()
                logger.info(f"{request.user} - updated card data.")

                return redirect('view_card_profile', card_profile_id=card_profile_id)

        else:
            form = EditProfile()
            logger.info(f"{request.user} - edit card profile {card_profile.id}")

        return render(request, 'card_profile/edit_card_profile.html', {'card_profile': card_profile, 'form': form})
    
    else:
        return render(request, 'core/message.html', {'message': 'You are not authorized to view this information'})


@login_required
def create_card_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES)

        if form.is_valid():
            new_card = form.save(commit=False)
            new_card.created_by = request.user
            new_card.page_title = f"{new_card.first_name} {new_card.last_name} - Nova Card"
            new_card.card_model = "1"
            new_card.save()
            logger.info(f"{request.user} - created card profile.")

            return redirect('dashboard')

    else:
        form = EditProfile()
        logger.info(f"{request.user} - create card profile")

    return render(request, 'card_profile/create_card_profile.html', {'form': form})


@login_required
def delete_card_profile(request, card_profile_id):
    card_profile = CardProfile.objects.filter(created_by=request.user).get(pk=card_profile_id)
    card_profile.delete()

    messages.success(request, 'The card profile was deleted successfully!')

    return redirect('dashboard')