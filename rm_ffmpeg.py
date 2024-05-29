import rm_live_info
import my_time

import json
import time
import os
import subprocess
import threading





def run_ffmpeg_cmd(live_label, record_level):
    file_path = '/' + 'RM' + my_time.get_date_str()
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    file_name = live_label + '_' + my_time.get_time_str() + '.mp4'
    live_url = live_info[live_label][record_level]
    ffmpeg_cmd = ffmpeg_head_cmd + '"' + live_url + '"' + ffmpeg_tail_cmd + file_path + '/' + file_name
    print('the ' + file_name + ' recorder cmd is: ')
    print(ffmpeg_cmd)
    print('')
    process = subprocess.Popen(ffmpeg_cmd, creationflags=subprocess.CREATE_NEW_CONSOLE, stdin=subprocess.PIPE)
    live_info[live_label]['process'] = process


def close_ffmpeg_cmd(live_label):
    print('the ' + live_label + ' recorder cmd is closed!')
    live_info[live_label]['process'].stdin.write(b'q')


def init_ffmpeg_recorder(live_label, record_level_dict):



def auto_reload():
    while True:
        for index in range(1, 14):
            if event.is_set():
                return
            if video_info[index]['url'] != '':
                if video_info[index]['process'].poll() is not None:
                    print('')
                    run_ffmpeg_cmd(index)
            time.sleep(3)


# for i in range(1, 14):
#     if video_info[i]['url'] != '':
#         run_ffmpeg_cmd(i)
#
# event = threading.Event()
#
# thread = threading.Thread(target=auto_reload, args=(event,))
# thread.start()
#
# while True:
#     input_str = output_path = input("Please enter q to quit: ")
#     if input_str == 'q':
#         break
#     else:
#         print('Your input is' + input_str + 'not q')
#
# event.set()
#
# time.sleep(10)








get_live_game_url = "https://pro-robomasters-hz-n5i3.oss-cn-hangzhou.aliyuncs.com/live_json/live_game_info.json"
live_game_info_dict = (get_live_game_info(get_live_game_url))
live_info = rm_live_info.get_live_info_dict(live_game_info_dict)

print(json.dumps(live_info, sort_keys=False, indent=4))

ffmpeg_head_cmd = 'ffmpeg -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -i '
ffmpeg_tail_cmd = ' -c:v copy -c:a copy -f mp4 '
