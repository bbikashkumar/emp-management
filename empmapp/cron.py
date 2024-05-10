import logging

logger = logging.getLogger(__name__)

def print_hello():
    print("django cron")
    logger.info("Cron job was called ")