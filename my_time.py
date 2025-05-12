import time


def get_time_str():
    now_time = time.strftime('%y%m%d_%H%M%S', time.localtime())
    return now_time


def get_date_str():
    now_time = time.strftime('%y%m%d', time.localtime())
    return now_time


def delay_until_time(str_time):
    str_time = str_time.replace(" ", "")

    if str_time == '':
        return

    while True:
        if int(str_time) < int(time.strftime('%Y%m%d%H%M%S', time.localtime())):
            return
        else:
            print('start time:' + str_time)
            print('now time  :' + time.strftime('%Y%m%d%H%M%S', time.localtime()))
            time.sleep(1)
