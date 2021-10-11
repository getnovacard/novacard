from django.db import models
import os
from uuid import uuid4


class Card_profile(models.Model):

    def path_and_rename(self, filename):
        upload_to = 'uploads'
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)

        return os.path.join(upload_to, filename)

    MALE = 'M'
    FEMALE = 'F'

    CHOICES_GENDER = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )

    username = models.CharField(max_length=255, unique=True)
    repository_name = models.CharField(max_length=255, unique=True)
    page_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    baseurl = models.CharField(max_length=255, default="/")
    url = models.URLField(max_length=200, unique=True)
    avatar = models.ImageField(upload_to=path_and_rename, height_field=None, width_field=None,
                               max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER)
    title = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
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
    markdown = models.CharField(max_length=255, default="kramdown")

    def __str__(self):
        return self.username
