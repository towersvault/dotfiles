import os
from glob import glob


def get_next_screenshot():
    from datetime import datetime
    new_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    return new_name
