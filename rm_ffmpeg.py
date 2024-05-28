import rm_live_info
import my_time

import json
import time
import os
import subprocess
import threading


ffmpeg_head_cmd = 'ffmpeg -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -i '
ffmpeg_tail_cmd = ' -c:v copy -c:a copy -f mp4 '


def run_ffmpeg_single_cmd(recorder_info, live_label):
    if recorder_info[live_label]['process'] is not None:
        return
    file_path = './' + 'RM' + my_time.get_date_str()
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    file_name = live_label + '_' + my_time.get_time_str() + '.mp4'
    live_url = recorder_info[live_label][recorder_info[live_label]["level"]]
    ffmpeg_cmd = ffmpeg_head_cmd + '"' + live_url + '"' + ffmpeg_tail_cmd + file_path + '/' + file_name
    print('the ' + file_name + ' recorder cmd is: ')
    print(ffmpeg_cmd)
    print('')
    process = subprocess.Popen(ffmpeg_cmd, creationflags=subprocess.CREATE_NEW_CONSOLE,
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # process = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    recorder_info[live_label]['process'] = process


def close_ffmpeg_single_cmd(recorder_info, live_label):
    if recorder_info[live_label]['process'] is None:
        return
    print('the ' + live_label + ' recorder cmd is closed!')
    recorder_info[live_label]['process'].stdin.write(b'q\r\n')
    recorder_info[live_label]['process'].stdin.flush()




