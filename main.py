import rm_live_info
import my_time
import rm_recorder

import json


get_live_game_url = "https://pro-robomasters-hz-n5i3.oss-cn-hangzhou.aliyuncs.com/live_json/live_game_info.json"
live_level = {"m": "1080p",
              "B": "1080p",
              "R": "1080p"}


rm_json_dict = rm_live_info.get_rm_json_dict(get_live_game_url)
zone_json = rm_live_info.get_zone(rm_json_dict)
main_url = rm_live_info.get_main_url(zone_json)
fpv_url = rm_live_info.get_fpv_url(zone_json)
live_url = rm_live_info.get_live_url(main_url, fpv_url)
recorder_info = rm_recorder.make_recorder_info(live_url, live_level)
print(json.dumps(recorder_info, sort_keys=False, indent=4))