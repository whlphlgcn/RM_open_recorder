import rm_ffmpeg
import subprocess


def make_recorder_info(live_url, live_level):
    for k in live_url.keys():
        live_url[k]["level"] = live_level[k]
        live_url[k]["process"] = None
    return live_url


def check_recorder_info(recorder_info):
    for k in recorder_info:
        while 1:
            if recorder_info[k]["level"] == 'disable':
                print("the " + k + " level is disable!")
                break
            elif recorder_info[k]["level"] in recorder_info[k]:
                print("the " + k + " level is " +
                      recorder_info[k]["level"])
                break
            elif recorder_info[k]["level"] == "1080p":
                recorder_info[k]["level"] = "720p"
                print("the " + k +
                      " level is 1080p, but the recorder is not support!")
                print("the " + k + " level is changed to 720p!")
            elif recorder_info[k]["level"] == "720p":
                recorder_info[k]["level"] = "540p"
                print("the " + k +
                      " level is 720p, but the recorder is not support!")
                print("the " + k + " level is changed to 540p!")
            elif recorder_info[k]["level"] == "540p":
                recorder_info[k]["level"] = "disable"
                print("the " + k +
                      " level is 540p, but the recorder is not support!")
                print("the " + k + " level is changed to disable!")
            else:
                print("the " + k + " level is " +
                      recorder_info[k]["level"] + ", but the recorder is not support!")
                print("the " + k + " level is changed to 1080p!")
                recorder_info[k]["level"] = "1080p"
    return recorder_info


def start_all_recorder(recorder_info):
    for k in recorder_info:
        if recorder_info[k]["level"] != 'disable':
            rm_ffmpeg.run_ffmpeg_single_cmd(recorder_info, k)


def close_all_recorder(recorder_info):
    for k in recorder_info:
        if recorder_info[k]["level"] != 'disable':
            rm_ffmpeg.close_ffmpeg_single_cmd(recorder_info, k)


def check_process_state(recorder_info):
    for k in recorder_info:
        if recorder_info[k]["level"] != 'disable':
            if recorder_info[k]["process"] is not None:
                if recorder_info[k]["process"].poll() is not None:
                    recorder_info[k]["process"] = None


def get_close_process_num(recorder_info):
    num = 0
    for k in recorder_info:
        if recorder_info[k]["level"] != 'disable':
            if recorder_info[k]["process"] is None:
                num += 1
    return num


def get_open_process_num(recorder_info):
    num = 0
    for k in recorder_info:
        if recorder_info[k]["level"] != 'disable':
            if recorder_info[k]["process"] is not None:
                num += 1
    return num
