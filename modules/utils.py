from uuid import uuid4
import os
import base64

from apps.card_profile.models import CardProfile
from project.settings import MEDIA_ROOT

def generate_vcf(card_profile):
    try:
        # Delete existing vcard file if any
        
        if card_profile.vcard:
            existing_vcard_filepath = f'media/{card_profile.vcard}'

            try:
                os.remove(existing_vcard_filepath)
            except:
                print("The indicated vcard file does not exist")
        new_vcard_filename = f'{uuid4().hex}.vcf'

        # Convert avatar image to base64
        avatar_filepath = f'media/{card_profile.avatar_image}'
        if card_profile.avatar_image:    
            with open(avatar_filepath, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            avatar_base64 = encoded_string.decode('utf-8')

        # Define social profiles list to be used during the update procedure
        social_profiles = [
            ("facebook", card_profile.facebook_url),
            ("linkedin", card_profile.linkedin_url),
            ("instagram", card_profile.instagram_url),
            ("pinterest", card_profile.pinterest_url),
            ("twitter", card_profile.twitter_url),
            ("youtube", card_profile.youtube_url),
            ("snapchat", card_profile.snapchat_url),
            ("whatsapp", card_profile.whatsapp_url),
            ("tiktok", card_profile.tiktok_url),
            ("telegram", card_profile.telegram_url),
            ("skype", card_profile.skype_url),
            ("github", card_profile.github_url),
            ("gitlab", card_profile.gitlab_url)
            ]

        # Create tmp directory
        try: 
            os.mkdir("tmp") 
        except OSError as error: 
            print(error)

        # Write to the new vcard file
        vcf_file = f'tmp/{new_vcard_filename}'
        f_vcf = open(vcf_file, "w")

        line = "BEGIN:VCARD\n"
        f_vcf.write(line)

        line = "VERSION:3.0\n"
        f_vcf.write(line)

        first_name = card_profile.first_name
        last_name = card_profile.last_name
        line = "N:" + last_name + ";" + first_name + ";;;\n"
        f_vcf.write(line)
        line = "FN:" + first_name + " " + last_name + "\n"
        f_vcf.write(line)

        if card_profile.avatar_image:   
            line = "PHOTO;ENCODING=b;TYPE=JPEG:" + avatar_base64 + "\n"
            f_vcf.write(line)

        if card_profile.title:
            line = "TITLE:" + card_profile.title + "\n"
            f_vcf.write(line)

        if card_profile.company:
            line = "ORG:" + card_profile.company + ";\n"
            f_vcf.write(line)

        if card_profile.email:
            line = "EMAIL;type=INTERNET;type=HOME;type=pref:" + card_profile.email + "\n"
            f_vcf.write(line)

        if card_profile.phone:
            line = "TEL;type=CELL;type=VOICE;type=pref:" + card_profile.phone + "\n"
            f_vcf.write(line)

        if card_profile.website:
            line = "item1.URL;type=pref:" + card_profile.website + "\n"
            f_vcf.write(line)
            line = "item1.X-ABLabel:_$!<HomePage>!$_\n"
            f_vcf.write(line)

        for profile in social_profiles:
            x = profile[0]
            y = profile[1]
            if profile[1]:
                line = "X-SOCIALPROFILE;type=" + profile[0] + ":" + profile[1] + "\n"
                f_vcf.write(line)

        line = "END:VCARD"
        f_vcf.write(line)

        current_vcard_path = vcf_file
        media_vcard_path = f'{MEDIA_ROOT}/{new_vcard_filename}'
        os.rename(current_vcard_path, media_vcard_path)

        cp = CardProfile.objects.get(pk=card_profile.id)
        cp.vcard = new_vcard_filename
        cp.save(update_fields=['vcard'])

        return 'The vcard was generated and saved accordingly'

    except:
        return 'The vcard was not properly generated,'


