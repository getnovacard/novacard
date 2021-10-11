from django import forms
from .models import Card_profile


class EditProfile(forms.ModelForm):
    class Meta:
        model = Card_profile
        fields = [
            'avatar',
            'first_name',
            'last_name',
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
        ]
        pass
