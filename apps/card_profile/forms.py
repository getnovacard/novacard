from django import forms
from .models import CardProfile


class EditProfile(forms.ModelForm):
    class Meta:
        model = CardProfile
        fields = [
            'avatar_image',
            'bg_image',
            'first_name',
            'last_name',
            'gender',
            'title',
            'company',
            'email',
            'phone',
            'website',
            'facebook_url',
            'linkedin_url',
            'instagram_url',
            'pinterest_url',
            'twitter_url',
            'youtube_url',
            'snapchat_url',
            'whatsapp_url',
            'tiktok_url',
            'telegram_url',
            'skype_url',
            'github_url',
            'gitlab_url',
            'card_name',
        ]
