def make_recorder_info(live_url, live_level):
    for k in live_url.keys():
        live_url[k]["level"] = live_level[k[0]]
        live_url[k]["process"] = None
    return live_url










