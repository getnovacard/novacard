import json
import shutil
import os
from project.settings import TASKS_DIR
from .utils import create_directory, get_random_string
import logging

logger =logging.getLogger('novacard_info')


def create_update_task(user_profile, form_instance):

    logger.info(f"---> attempting creation of main tasks directory")
    tasks_directory = TASKS_DIR
    create_directory(tasks_directory)

    logger.info(f"---> creating update task directory for user {user_profile.username}")
    individual_task_directory = f"{tasks_directory}task_{get_random_string(10)}"    
    create_directory(individual_task_directory)

    logger.info(f"---> checking if new avatar image was uploaded in order to set the 'update_avatar' variable")
    try:
        avatar_image_exists = form_instance.files['avatar']
        update_avatar = "1"
    except:
        update_avatar = "0"
    logger.info(f"---> update_avatar = {update_avatar}")

    avatar_file_name = user_profile.avatar.path.split("/")[-1]
    avatar_file_path = f"media/{str(user_profile.avatar)}"
    avatar_file_extension = os.path.splitext(avatar_file_name)[1]
    task_avatar_filename = f"avatar{avatar_file_extension}"

    if update_avatar == "1":
        logger.info(f"---> avatar_filename = {avatar_file_name}; avatar_file_path = {avatar_file_path}; avatar_file_extension = {avatar_file_extension}; task_avatar_filename = {task_avatar_filename}")
        logger.info(f"---> copying avatar image for user {user_profile.username} to temporary task directory")
        task_avatar_file_path =f"{individual_task_directory}/{task_avatar_filename}"
        shutil.copyfile(avatar_file_path, task_avatar_file_path)

    logger.info(f"---> creating 'operations_dict' for user {user_profile.username}")
    operations_dict = {
        "username": user_profile.username,
        "repository": user_profile.repository_name,
        "update_avatar": update_avatar,
        "config": {
            "page_title": user_profile.page_title,
            "description": user_profile.description,
            "baseurl": user_profile.baseurl,
            "url": user_profile.url,
            "avatar": task_avatar_filename,
            "contact": {
                "contact-first_name": "" if form_instance.instance.first_name is None else form_instance.instance.first_name,
                "contact-last_name": "" if form_instance.instance.last_name is None else form_instance.instance.last_name,
                "contact-title": "" if form_instance.instance.title is None else form_instance.instance.title,
                "contact-company": "" if form_instance.instance.company is None else form_instance.instance.company,
                "contact-email": "" if form_instance.instance.email is None else form_instance.instance.email,
                "contact-phone": "" if form_instance.instance.phone is None else form_instance.instance.phone,
                "contact-website": "" if form_instance.instance.website is None else form_instance.instance.website,
                "contact-facebook_url": "" if form_instance.instance.facebook_url is None else form_instance.instance.facebook_url,
                "contact-linkedin_url": "" if form_instance.instance.linkedin_url is None else form_instance.instance.linkedin_url,
                "contact-instagram_url": "" if form_instance.instance.instagram_url is None else form_instance.instance.instagram_url,
                "contact-pinterest_url": "" if form_instance.instance.pinterest_url is None else form_instance.instance.pinterest_url,
                "contact-twitter_url": "" if form_instance.instance.twitter_url is None else form_instance.instance.twitter_url,
                "contact-youtube_url": "" if form_instance.instance.youtube_url is None else form_instance.instance.youtube_url,
                "contact-snapchat_url": "" if form_instance.instance.snapchat_url is None else form_instance.instance.snapchat_url,
                "contact-whatsapp_url": "" if form_instance.instance.whatsapp_url is None else form_instance.instance.whatsapp_url,
                "contact-tiktok_url": "" if form_instance.instance.tiktok_url is None else form_instance.instance.tiktok_url,
                "contact-telegram_url": "" if form_instance.instance.telegram_url is None else form_instance.instance.telegram_url,
                "contact-skype_url": "" if form_instance.instance.skype_url is None else form_instance.instance.skype_url,
                "contact-github_url": "" if form_instance.instance.github_url is None else form_instance.instance.github_url,
                "contact-gitlab_url": "" if form_instance.instance.gitlab_url is None else form_instance.instance.gitlab_url
            }
        }                                              
    }

    operations_file = f"{individual_task_directory}/operations.json"
    with open(operations_file, "w") as f:
        json.dump(operations_dict, f)

    logger.info(f"---> update task directory for user {user_profile.username} created successfully")
    return individual_task_directory
