import os
import subprocess
import json
from pathlib import Path

from project.settings import TEMP_DIR
from .modules.utils import create_directory, run_bash_command, delete_directory, get_random_string
from .modules.core import update_profile_c, update_avatar_c, generate_vcf_c

from celery.utils.log import get_task_logger
logger = get_task_logger('novacard_info')


def update_profile(operations_directory):
    logger.info(f"---> updating novacard profile from directory {operations_directory}")

    # - Importing configurations from "config.json"
    cwd = Path(__file__).parents[0]
    config_file = f'{cwd}/config.json'

    logger.info(f"---> importing update procedure configuration from {config_file}")
    with open(config_file, 'r') as f:
        config_string = f.read()
    config = json.loads(config_string)

    remote_account = config["remote_account"]
    logger.info(f"---> remote account used: {remote_account}")

    # Importing the operations to be performed from the "operations.json" file
    operations_file = f'{operations_directory}/operations.json'

    logger.info(f"---> importing update procedure operations file from {operations_file}")
    with open(operations_file, 'r') as f:
        operations_string = f.read()
    operations = json.loads(operations_string)

    repository_name = operations["repository"]
    

    avatar_update = True if operations["update_avatar"] == "1" else False
    vcf_generate = True if (operations.get('config').get('contact') is not None) \
                        and (operations.get('config').get('contact') != "") else False
    logger.info(f"---> repository_name = {repository_name}; avatar_update = {avatar_update}; vcf_generate = {vcf_generate}")

    # Creating temporary directory structure used for the update operation
    logger.info(f"---> creating temporary directory structure used for the update operation")
    temp_dir = TEMP_DIR
    logger.info(f"---> attempting creation of directory {temp_dir}")
    create_directory(temp_dir)

    random_string = get_random_string(10)
    update_dir = f'{temp_dir}{repository_name}-{random_string}' 
    logger.info(f"---> attempting creation of directory {update_dir}")
    create_directory(update_dir)

    # Clone the remote git repository to update
    remote_repo = f'{remote_account}{repository_name}'
    logger.info(f"---> cloning remote repository {remote_repo} to temporary update directory")
    clone_command = f'git clone {remote_repo} {update_dir}'
    run_bash_command(clone_command)

    updated = []

    # Update profile _config file
    update_profile_c(update_dir, operations)
    updated.append("config")

    # Update profile avatar
    if avatar_update:
        update_avatar_c(update_dir, operations_directory, operations)
        updated.append("avatar")

    if vcf_generate:
        generate_vcf_c(update_dir, operations)
        updated.append("vcard")

    # Commit and push changes to remote repository
    commit_message = f"updated: {updated}"
    commit_command = f"cd {update_dir} && git add . && git commit -m '{commit_message}' && git push origin master"
    logger.info(f"---> committing changes to remote repository {remote_repo}")
    subprocess.call(commit_command, shell=True)

    #logger.info(f"---> removing the temporary update directory {update_dir}")
    #delete_directory(update_dir)

    logger.info(f"---> update procedure completed successfully")
