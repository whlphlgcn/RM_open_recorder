import json
import time
import urllib.request
import ssl


rm_fpv_name2my_name_dict = {"红方英雄": "R1",
                            "蓝方英雄": "B1",
                            "红方工程": "R2",
                            "蓝方工程": "B2",
                            "红方3号步兵": "R3",
                            "蓝方3号步兵": "B3",
                            "红方4号步兵": "R4",
                            "蓝方4号步兵": "B4",
                            "红方空中": "R6",
                            "蓝方空中": "B6", }


def get_zone(rm_json):
    for eventData_i in rm_json["eventData"]:
        if time.strftime('%Y-%m-%d', time.localtime()) in eventData_i["zoneDate"]:
            print("today is " + eventData_i["zoneName"] + "!")
            return eventData_i
    print("today is not RM live day!")
    return None


def get_main_url(zone_json, main_live_url=None):
    if main_live_url is None:
        main_live_url = {}
    for zoneLiveString_i in zone_json["zoneLiveString"]:
        main_live_url[zoneLiveString_i["label"]] = zoneLiveString_i["src"]
    return main_live_url


def get_fpv_url(zone_json, fpv_live_url=None):
    if fpv_live_url is None:
        fpv_live_url = {}
    for fpvData_i in zone_json["fpvData"]:
        my_name = rm_fpv_name2my_name_dict[fpvData_i["role"]]
        fpv_live_url[my_name] = {}
        for sources_i in fpvData_i["sources"]:
            fpv_live_url[my_name][sources_i["label"]] = sources_i["src"]
        # print(fpv_live_url)
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
