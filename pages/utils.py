import datetime
import logging
import random
import string
from time import sleep

from constants.text_example import ENG_TEXT


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_str(lenght=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(lenght))


def wait_until_ok(timeout=5, period=0.25):
    """Retries function until ok"""
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def text_example(length=15, preset=ENG_TEXT):
    """Create text by using example"""
    words = preset.split(" ")
    return ' '.join(random.choice(words) for _ in range(length))


def log_wrapper(func):
    """Add logs and metrics by using docstring"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecorator]")
        result = func(*args, **kwargs)
        log.info(f"{func.__doc__}")
        return result

    return wrapper


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password
        self.posts = []

    def fill_properties(self):
        """Generate random values for user fields"""
        variety = random_num()
        self.username = f"{random_str()}{variety}"
        self.email = f"{self.username}@gmail.com"
        self.password = f"Qwerty{variety}"
