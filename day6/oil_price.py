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


#推荐使用lxml(pip install lxml)
if response.status_code == 200:
    # html.parser 是python内置解析器
    # soup = BeautifulSoup(response.text, 'html.parser')
    soup = BeautifulSoup(response.text, 'lxml')

    target_div_id='youjia'
    target_div = soup.find('div', id=target_div_id)
    #  find_all():返回所有匹配;find():返回第一个匹配
    dl_tags = target_div.find_all('dl')

    result = []
    for x in dl_tags:
        # 获取第一个 <dt> 标签中的文本内容
        name = x.find('dt').get_text()
        price = x.find('dd').get_text()
        result.append({'name':name, 'price':price})
    print('-----------------抓到数据------------')
    print(result)
else:
    print('请求失败')