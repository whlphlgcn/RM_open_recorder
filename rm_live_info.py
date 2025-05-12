import json
import time
import urllib.request
import ssl


my_name2rm_fpv_name2_dict = {"R1": ["红", "英雄"],
                             "B1": ["蓝", "英雄"],
                             "R2": ["红", "工程"],
                             "B2": ["蓝", "工程"],
                             "R3": ["红", "3", "步兵"],
                             "B3": ["蓝", "3", "步兵"],
                             "R4": ["红", "4", "步兵"],
                             "B4": ["蓝", "4", "步兵"],
                             "R5": ["红", "5", "步兵"],
                             "B5": ["蓝", "5", "步兵"],
                             "R6": ["红", "无人机"],
                             "B6": ["蓝", "无人机"],
                             "RALL": ["红", "全"],
                             "BALL": ["蓝", "全"]}


def get_zone_auto(rm_json):
    for eventData_i in rm_json["eventData"]:
        if time.strftime('%Y-%m-%d', time.localtime()) in eventData_i["zoneDate"]:
            print("today is " + eventData_i["zoneName"] + "!")
            return eventData_i
    print("today is not RM live day!")
    return None


def get_zone_name_list(rm_json):
    zone_list = []
    for eventData_i in rm_json["eventData"]:
        zone_list.append(eventData_i["zoneName"])
    return zone_list


def get_zone_by_name(rm_json, zone_name):
    for eventData_i in rm_json["eventData"]:
        if zone_name == eventData_i["zoneName"]:
            return eventData_i
    return None


def get_main_url(zone_json, main_live_url=None):
    if main_live_url is None:
        main_live_url = {}
    for zoneLiveString_i in zone_json["zoneLiveString"]:
        main_live_url[zoneLiveString_i["label"]] = zoneLiveString_i["src"]
    return main_live_url


def get_fpv_url(zone_json):
    fpv_live_url = {}
    for my_name, rm_fpv_name2_list in my_name2rm_fpv_name2_dict.items():
        fpv_live_url[my_name] = {}
        for fpvData_i in zone_json["fpvData"]:
            name_hit_cnt = 0
            for rm_fpv_name2_list_i in rm_fpv_name2_list:
                if rm_fpv_name2_list_i in fpvData_i["role"]:
                    name_hit_cnt += 1
                    # print("hit " + my_name + " " + rm_fpv_name2_list_i + " " + fpvData_i["role"])
            if name_hit_cnt == len(rm_fpv_name2_list):
                for sources_i in fpvData_i["sources"]:
                    fpv_live_url[my_name][sources_i["label"]
                                          ] = sources_i["src"]
                break
    return fpv_live_url


def get_live_url(main_url, fpv_url):
    live_url = {"main": main_url}
    live_url.update(fpv_url)
    return live_url


def get_rm_json_dict(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    json_data = json.loads(data)
    return json_data
