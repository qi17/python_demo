target_url = 'http://www.qiyoujiage.com/guangdong.shtml'

# 构建header
header = {
    'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'cookie': '__tins__5547870=%7B%22sid%22%3A%201762867466692%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201762869266692%7D; __51cke__=; __51laig__=1; Hm_lvt_5f6aa820742249510b43a8fd7e30bb7d=1762853377,1762867467; Hm_lpvt_5f6aa820742249510b43a8fd7e30bb7d=1762867467;'
}

# 用到了两个库 request 和 bs4
import requests
from bs4 import BeautifulSoup

response = requests.get(target_url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

# 还要学一下获取标签
target_div_id='youjia'
target_div = soup.find('div', id=target_div_id)

dl_tags = target_div.find_all('dl')

result = []
for x in dl_tags:
    name = x.find('dt').extract()
    price = x.find('dd').extract()
    result.append({'name':name, 'price':price})

print(result)
