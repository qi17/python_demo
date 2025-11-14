"""
抓取天气信息
"""

# 1.先获取各个城市天气编码
city_code = '101280102'
weather = 'https://e.weather.com.cn/mweather/%s' % city_code + '.shtml'
# 构建header
header = {
    'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'Referer': 'https://e.weather.com.cn/'
}
import requests
from bs4 import BeautifulSoup
import time

# 今日天气
url = 'https://d1.weather.com.cn/weather_index/101280102.html'
response = requests.get(url,
                        headers=header,
                        params={'_': int(time.time() * 1000)}, )
response.encoding = 'utf-8'

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    context = soup.find('body').get_text()
    print(context)

# todo 使用json-repair库解析json