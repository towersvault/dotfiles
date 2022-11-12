import os
from glob import glob
import subprocess


def get_next_screenshot():
    from datetime import datetime
    new_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    return new_name


def get_next_screenshot_new():
    result = subprocess.run(['date', '+"%Y%m%d_%H%M%S"'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
