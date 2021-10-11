from celery import shared_task
from modules.operations.update_profile import update_profile
from project.celery import app

from celery.utils.log import get_task_logger
logger = get_task_logger('novacard_info')


@app.task
def update_profile_task(individual_task_directory):

    logger.info(f"---> running update task from path {individual_task_directory}")
    update_profile(individual_task_directory)

    return "Done"