import datetime
import os


def date_time():
    date = "%d-%m-%Y"
    time = "%H-%M-%S"
    return date, time


def get_date_timestamp():
    date, time = date_time()
    return datetime.datetime.now().strftime(date + "_" + time)


def get_datestamp():
    date, time = date_time()
    return datetime.datetime.now().strftime(date)


def get_timestamp():
    date, time = date_time()
    return datetime.datetime.now().strftime(time)


def create_dir(dir_path):
    os.makedirs(dir_path, exist_ok=True)


def generate_report_filename():
    current_time = get_date_timestamp()
    return f"Test_Execution_Report_{current_time}.html"




