import rm_live_info
import my_time
import json


get_live_game_url = "https://pro-robomasters-hz-n5i3.oss-cn-hangzhou.aliyuncs.com/live_json/live_game_info.json"
rm_json = rm_live_info.get_live_game_info(get_live_game_url)
zone_json = rm_live_info.get_zone(rm_json)
main_url = rm_live_info.get_main_url(zone_json)
fpv_url = rm_live_info.get_fpv_url(zone_json)
live_url = rm_live_info.get_live_url(main_url, fpv_url)
print(json.dumps(live_url, sort_keys=False, indent=4))











