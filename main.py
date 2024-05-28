import time

import rm_live_info
import my_time
import rm_recorder
import rm_ffmpeg

import json
import pprint
import subprocess
import threading


get_live_game_url = "https://pro-robomasters-hz-n5i3.oss-cn-hangzhou.aliyuncs.com/live_json/live_game_info.json"
live_level = {"main": "1080p",
              "B1": "1080p",
              "B2": "1080p",
              "B3": "1080p",
              "B4": "1080p",
              "B6": "1080p",
              "R1": "1080p",
              "R2": "1080p",
              "R3": "1080p",
              "R4": "1080p",
              "R6": "1080p"}
recorder_state = 'init'
recorder_start_time = '2024 05 28 21 32 10'
# recorder_start_time = ''


def auto_start_and_close_thread():
    global recorder_state
    global recorder_info
    while True:
        time.sleep(1)
        if recorder_state == 'init':
            rm_recorder.start_all_recorder(recorder_info)
            recorder_state = 'recording'

        elif recorder_state == 'recording':
            rm_recorder.check_process_state(recorder_info)
            if rm_recorder.get_close_process_num(recorder_info) != 0:
                rm_recorder.start_all_recorder(recorder_info)

        elif recorder_state == 'quit':
            rm_recorder.check_process_state(recorder_info)
            if rm_recorder.get_open_process_num(recorder_info) != 0:
                rm_recorder.close_all_recorder(recorder_info)
            else:
                recorder_state = 'finish'

        elif recorder_state == 'finish':
            break


my_time.delay_until_time(recorder_start_time)

rm_dict = rm_live_info.get_rm_json_dict(get_live_game_url)
zone_dict = rm_live_info.get_zone(rm_dict)

if zone_dict is None:
    zone_dict = rm_dict["eventData"][0]

main_url = rm_live_info.get_main_url(zone_dict)
fpv_url = rm_live_info.get_fpv_url(zone_dict)
live_url = rm_live_info.get_live_url(main_url, fpv_url)
recorder_info = rm_recorder.make_recorder_info(live_url, live_level)

pprint.pprint(recorder_info)

thread = threading.Thread(target=auto_start_and_close_thread)
thread.start()

time.sleep(10)

while True:
    input_str = output_path = input("Please enter q to quit: ")
    if input_str == 'q':
        recorder_state = 'quit'
        break
    else:
        print('Your input is ' + input_str + ' not q')

while recorder_state != 'finish':
    pass

exit()



