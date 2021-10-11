import os
import random
import string
import logging

logger =logging.getLogger('novacard_info')


def create_directory(directory):
    check_dir = os.path.isdir(directory)

    if not check_dir:
        os.makedirs(directory)
        logger.info(f"---> created directory {directory}")
    else:
        logger.info(f"---> {directory} already exists")


def get_random_string(length):
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(length)))
    logger.info(f"---> generating random string for profile update directory {result_str}")
    
    return result_str
