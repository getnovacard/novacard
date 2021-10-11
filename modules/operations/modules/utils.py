import subprocess
import os
import shutil
import random
import string
import base64

from celery.utils.log import get_task_logger
logger = get_task_logger('novacard_info')


def create_directory(directory):
    check_dir = os.path.isdir(directory)

    if not check_dir:
        os.makedirs(directory)
        logger.info(f"---> created directory {directory}")
    else:
        logger.info(f"---> {directory} already exists")


def run_bash_command(command):
    logger.info(f"---> running bash command '{command}'")
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

    output, error = process.communicate()
    logger.info(str(output))


def empty_directory(directory_path):
    logger.info(f"---> attempting to empty out the directory {directory_path}")
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            logger.info(f"---> failed to delete {file_path}; reason {e}") 


def delete_directory(directory_path):
    logger.info(f"---> attempting to delete directory {directory_path}")
    if os.path.exists(directory_path):
        if len(os.listdir(directory_path)) == 0:
            os.rmdir(directory_path)
        else:
            empty_directory(directory_path)
            os.rmdir(directory_path)
    else:
        logger.info(f"---> the directory {directory_path} does not exist")   


def get_random_string(length):
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(length)))
    logger.info(f"---> generating random string for profile update directory {result_str}")
    
    return result_str


def convert_file_to_base64(file_path):
    logger.info(f"---> converting the file {file_path} to base64")
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    
    return encoded_string.decode('utf-8')
