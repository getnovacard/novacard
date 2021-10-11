from django.shortcuts import render
import logging

logger =logging.getLogger('novacard_info')


def frontpage(request):
    logger.info(f"{request.user} - access frontpage")
    return render(request, 'core/frontpage.html')

