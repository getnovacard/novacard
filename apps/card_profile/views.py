from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
import logging
import mimetypes

from .models import CardProfile
from .forms import EditProfile
from apps.template.models import Template
from modules.utils import generate_vcf
from project.settings import MEDIA_ROOT


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
    templates = Template.objects.all()

    if request.user.id == card_profile.created_by.id:
        if request.method == 'POST':
            form = EditProfile(request.POST, request.FILES, instance=card_profile)

            if form.is_valid():
                profile_change = form.save(commit=False)
                profile_change.created_by = request.user
                profile_change.save()
                logger.info(f"{request.user} - updated card data.")

                return_message = generate_vcf(card_profile)

                return redirect('view_card_profile', card_profile_id=card_profile_id)

        else:
            form = EditProfile()
            logger.info(f"{request.user} - edit card profile {card_profile.id}")

        return render(request, 'card_profile/edit_card_profile.html', {'card_profile': card_profile, 'form': form, 'templates': templates})
    
    else:
        return render(request, 'core/message.html', {'message': 'You are not authorized to view this information'})


@login_required
def create_card_profile(request):
    templates = Template.objects.all()

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES)

        if form.is_valid():
            new_card = form.save(commit=False)
            new_card.created_by = request.user
            new_card.page_title = f"{new_card.first_name} {new_card.last_name} - Nova Card"
            new_card.card_model = "1"
            new_card.save()
            logger.info(f"{request.user} - created card profile.")

            new_profile_id = new_card.id
            card_profile = get_object_or_404(CardProfile, pk=new_profile_id)
            generate_vcf(card_profile)

            return redirect('dashboard')

    else:
        form = EditProfile()
        logger.info(f"{request.user} - create card profile")

    return render(request, 'card_profile/create_card_profile.html', {'form': form, 'templates': templates})


@login_required
def delete_card_profile(request, card_profile_id):
    card_profile = CardProfile.objects.filter(created_by=request.user).get(pk=card_profile_id)
    card_profile.delete()

    messages.success(request, 'The card profile was deleted successfully!')

    return redirect('dashboard')


def download_vcard(request, card_profile_id):
    card_profile = CardProfile.objects.get(pk=card_profile_id)
    vcard_filepath = f"{MEDIA_ROOT}/{card_profile.vcard}"
    vcard_filename = card_profile.vcard

    f = open(vcard_filepath, "r")
    mime_type, _ = mimetypes.guess_type(vcard_filepath)
    response = HttpResponse(f, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=vcard.vcf"

    return response