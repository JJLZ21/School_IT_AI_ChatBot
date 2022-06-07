import requests


def get_time():
    url = "http://worldtimeapi.org/api/timezone/America/Los_Angeles"
    res = requests.get(url)
    res = res.json()["datetime"]
    year = res[0:4]
    month = res[5:7]
    day = res[8:10]
    time = month+"/"+day+"/"+year
    return time
