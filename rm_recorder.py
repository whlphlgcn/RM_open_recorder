import rm_ffmpeg
import subprocess


def make_recorder_info(live_url, live_level):
    for k in live_url.keys():
        live_url[k]["level"] = live_level[k]
        live_url[k]["process"] = None
    return live_url


def start_all_recorder(recorder_info):
    for k in recorder_info:
        rm_ffmpeg.run_ffmpeg_single_cmd(recorder_info, k)


def close_all_recorder(recorder_info):
    for k in recorder_info:
        rm_ffmpeg.close_ffmpeg_single_cmd(recorder_info, k)


def check_process_state(recorder_info):
    for k in recorder_info:
        if recorder_info[k]["process"].poll() is not None:
            recorder_info[k]["process"] = None


def get_close_process_num(recorder_info):
    num = 0
    for k in recorder_info:
        if recorder_info[k]["process"] is None:
            num += 1
    return num


def get_open_process_num(recorder_info):
    num = 0
    for k in recorder_info:
        if recorder_info[k]["process"] is not None:
            num += 1
    return num








