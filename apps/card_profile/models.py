from django.contrib.auth.models import User
from django.db import models
import os
from uuid import uuid4


class CardProfile(models.Model):

    def path_and_rename(self, filename):
        upload_to = ''
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)

        return os.path.join(upload_to, filename)

    MALE = 'M'
    FEMALE = 'F'

    CHOICES_GENDER = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )

    card_name = models.CharField(max_length=255, unique=True, blank=False, null=False)
 
    page_title = models.CharField(max_length=255, blank=False, null=False)

    card_model = models.CharField(max_length=255, blank=False, null=False)

    avatar_image = models.ImageField(upload_to=path_and_rename, height_field=None, width_field=None,
                               max_length=255, blank=True, null=True)
    bg_image = models.ImageField(upload_to=path_and_rename, height_field=None, width_field=None,
                               max_length=255, blank=True, null=True)

    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER, blank=False, null=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    facebook_url = models.URLField(max_length=200, blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    instagram_url = models.URLField(max_length=200, blank=True, null=True)
    pinterest_url = models.URLField(max_length=200, blank=True, null=True)
    twitter_url = models.URLField(max_length=200, blank=True, null=True)
    youtube_url = models.URLField(max_length=200, blank=True, null=True)
    snapchat_url = models.URLField(max_length=200, blank=True, null=True)
    whatsapp_url = models.URLField(max_length=200, blank=True, null=True)
    tiktok_url = models.URLField(max_length=200, blank=True, null=True)
    telegram_url = models.URLField(max_length=200, blank=True, null=True)
    skype_url = models.URLField(max_length=200, blank=True, null=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    gitlab_url = models.URLField(max_length=200, blank=True, null=True)

    created_by = models.ForeignKey(User, related_name='card_profile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    changed_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.card_name
