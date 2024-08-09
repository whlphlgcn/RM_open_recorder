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
recorder_state = 'init'


# 该选项可以设置清晰度 1080p or 720p or 540p
# 清晰度越低，对网络环境要求越低
# 如果网络带宽不足(例如：50Mbps下行)
# 或者网络波动大(例如：信号差的wifi，或者有线网络但是宽带的运营商很垃圾)
# 请选择 540p
# 如果不想录制某视角，请填写 disable(字符串"disable")
live_level = {"main": "1080p",
              "B1": "1080p",
              "B2": "1080p",
              "B3": "1080p",
              "B4": "1080p",
              "B5": "1080p",
              "B6": "1080p",
              "R1": "1080p",
              "R2": "1080p",
              "R3": "1080p",
              "R4": "1080p",
              "R5": "1080p",
              "R6": "1080p",
              "ALL": "1080p"}


# 格式必须为xxxx年xx月xx日xx时xx分xx秒
# xx时为24小时制
# 例如 2024 05 29 08 25 00 是合理的定时字符串
# 例如 2024 5 29 8 25 0是不合理的！！！！！！
# 例如 24 05 29 08 25 00也是不合理的！！！！！！
# 不想启用定时录制功能可以令recorder_start_time = ''
recorder_start_time = '2024 08 09 12 10 00'  # 定时启动录制功能


# 建议使用vscode终端或者cmd终端启动，不建议通过其他方式启动(例如pycharm)
# 启动后，如果想退出，请在启动Python脚本的终端里反复输入q与回车
# 使用其他方法退出可能导致录制的视频文件损坏


def auto_start_and_close_thread():
    global recorder_state
    global recorder_info
    while True:
        if recorder_state == 'init':
            rm_recorder.start_all_recorder(recorder_info)
            recorder_state = 'recording'

        elif recorder_state == 'recording':
            rm_recorder.check_process_state(recorder_info)
            if rm_recorder.get_close_process_num(recorder_info) != 0:
                rm_recorder.check_process_state(recorder_info)
                rm_recorder.start_all_recorder(recorder_info)

        elif recorder_state == 'quit':
            rm_recorder.check_process_state(recorder_info)
            if rm_recorder.get_open_process_num(recorder_info) != 0:
                rm_recorder.check_process_state(recorder_info)
                rm_recorder.close_all_recorder(recorder_info)
            else:
                recorder_state = 'finish'

        elif recorder_state == 'finish':
            break

        time.sleep(10)


my_time.delay_until_time(recorder_start_time)

rm_dict = rm_live_info.get_rm_json_dict(get_live_game_url)
zone_dict = rm_live_info.get_zone(rm_dict)

if zone_dict is None:
    zone_dict = rm_dict["eventData"][4]

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



