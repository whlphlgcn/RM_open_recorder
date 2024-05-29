import time


def get_time_str():
    now_time = time.strftime('%y%m%d_%H%M%S', time.localtime())
    return now_time


def get_date_str():
    now_time = time.strftime('%y%m%d', time.localtime())
    return now_time

