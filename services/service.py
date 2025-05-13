import string
import random


def generate_short_id(size=6):
    """Генерирует сокращенный идентификатор"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(size))
