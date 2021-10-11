from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Card_profile
from .forms import EditProfile
from modules.core import create_update_task
from .tasks import update_profile_task
import logging

logger =logging.getLogger('novacard_info')

@login_required
def profiles_list(request):
    logger.info(f"{request.user} - access profiles_list")
    profiles = Card_profile.objects.all()

    return render(request, 'card_profile/profiles_list.html', {'profiles': profiles})


@login_required
def view_profile(request, username):
    logger.info(f"{request.user} - view profile {username}")
    user_profile = get_object_or_404(Card_profile, username=username)

    return render(request, 'card_profile/view_profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request, username):
    user_profile = get_object_or_404(Card_profile, username=username)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()

                
            if len(form.changed_data) > 0:
                logger.info(f"{request.user} - form data changed; a task will be created.")
                individual_task_directory = create_update_task(user_profile, form)
                logger.info(f"{request.user} - scheduling update task from path {individual_task_directory}")
                update_profile_task.delay(individual_task_directory)
                logger.info(f"{request.user} - save changes to profile {username}")

            logger.info(f"{request.user} - leaving update form; no changes detected")
            return redirect('view_profile', username=user_profile.username)

    else:
        form = EditProfile()
        logger.info(f"{request.user} - edit profile {username}")

    return render(request, 'card_profile/edit_profile.html', {'user_profile': user_profile, 'form': form})
