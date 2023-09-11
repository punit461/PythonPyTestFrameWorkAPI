import functools
import logging
import os

from configs.config import ConfigReader
from tests import project_directory

config_reader = ConfigReader()


def setup_custom_logger(name):
    log_dir = os.path.join(project_directory, "reports", "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Read log_mode and generate logs based on it.
    log_mode = config_reader.get_log_mode()

    if log_mode == "each_test_case_log_file":
        log_file = os.path.join(log_dir, f'{name}.log')
    else:
        log_file = os.path.join(log_dir, 'logs.log')

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


def logmethod(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = setup_custom_logger(func.__name__)

        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully.")
            return result
        except Exception as e:
            logger.error(f"Test {func.__name__} FAILED")
            logger.exception(e)
            raise e
        finally:
            logger.info(f"Finished test: {func.__name__}")

    return wrapper
