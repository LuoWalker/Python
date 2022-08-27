"""
北鲁坡村：
经纬：115.92762229769 39.541347511935

彩云API：
Token：sw2LVIjbsU08prHl
实时天气数据 API:  https://api.caiyunapp.com/v2.5/{Token}/{经度, 纬度}/realtime.json
示范 URL:  https://api.caiyunapp.com/v2.6/sw2LVIjbsU08prHl/121.6544,25.1552/realtime.json
天气现象：https://docs.caiyunapp.com/docs/tables/skycon
"""
import json
import requests
import sys
import pprint
import bs4


def get_key(val):
    for k, v in skycon_chart.items():
        if v == val:
            return k


# 对照表
skycon_chart = {'晴（白天）': 'CLEAR_DAY',
                '晴（夜间）': 'CLEAR_NIGHT',
                '多云（白天）': 'PARTLY_CLOUDY_DAY',
                '多云（夜间）': 'PARTLY_CLOUDY_NIGHT',
                '阴': 'CLOUDY',
                '轻度雾霾': 'LIGHT_HAZE',
                '中度雾霾': 'MODERATE_HAZE',
                '重度雾霾': 'HEAVY_HAZE',
                '小雨': 'LIGHT_RAIN',
                '中雨': 'MODERATE_RAIN',
                '大雨': 'HEAVY_RAIN',
                '暴雨': 'STORM_RAIN',
                '雾': 'FOG',
                '小雪': 'LIGHT_SNOW',
                '中雪': 'MODERATE_SNOW',
                '大雪': 'HEAVY_SNOW',
                '暴雪': 'STORM_SNOW',
                '浮尘': 'DUST',
                '沙尘': 'SAND',
                '大风': 'WIND'}


# 实时天气数据
token = 'sw2LVIjbsU08prHl'
location = ','.join(sys.argv[1:])
hours = 2
caiyun_realtime_url = 'https://api.caiyunapp.com/v2.6/%s/%s/realtime.json' % (
    token, location)

res = requests.get(caiyun_realtime_url)
res.raise_for_status()

weather_data = json.loads(res.text)
weather_realtime = weather_data['result']['realtime']

# pprint.pprint(weather_realtime)
weather_realtime['skycon'] = get_key(weather_realtime['skycon'])
weather_print = {'天气': weather_realtime['skycon'], '温度': weather_realtime['temperature'],
                 '体感温度': weather_realtime['apparent_temperature'], '相对湿度': weather_realtime['humidity'], }
print("当前温度：")
for k, v in weather_print.items():
    print(f'{k.rjust(4,"　")}:{v}')
print('---')

# 小时级预报
caiyun_hourly_url = 'https://api.caiyunapp.com/v2.6/%s/%s//hourly?hourlysteps=%d' % (
    token, location, hours)

res = requests.get(caiyun_hourly_url)
res.raise_for_status()

weather_data = json.loads(res.text)
weather_hourly = weather_data['result']['hourly']

# pprint.pprint(weather_hourly)
print("预告：")
print(weather_hourly['description'])
for hour in range(hours):
    print(f'{hour}小时后：')
    weather_hourly['skycon'][hour]['value'] = get_key(
        weather_hourly['skycon'][hour]['value'])
    weather_print[hour] = {'天气': weather_hourly['skycon'][hour]['value'], '温度': weather_hourly['temperature'][hour]['value'],
                           '体感温度': weather_hourly['apparent_temperature'][hour]['value'], '相对湿度': weather_hourly['humidity'][hour]['value'], }

    for k, v in weather_print[hour].items():
        print(f'{k.rjust(4,"　")}:{v}')
    print('---')
