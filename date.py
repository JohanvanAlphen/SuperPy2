# Imports

import os
from datetime import datetime, date


def handle_date(date_string):
    try:
        if date_string != datetime.strptime(date_string, "%Y-%m-%d").strftime(
            "%Y-%m-%d"
        ):
            raise ValueError
        return True
    except ValueError:
        return False


def create_date_txt():
    if not os.path.exists('date.txt'):
        current_date = date.today()
        current_date = current_date.strftime("%Y-%m-%d")
        file = open('date.txt', 'w')
        file.write(current_date)
        file.close()
