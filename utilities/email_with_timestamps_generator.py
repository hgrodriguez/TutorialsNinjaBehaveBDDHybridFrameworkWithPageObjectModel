"""Email module"""
from datetime import datetime


def get_new_email_with_timestamp():
    """Create new mail"""
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amotoori" + time_stamp + "@gmail.com"
