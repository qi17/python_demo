file_name='../doc/weather_city_code.txt'

pattern = r'“([^”]+)”\s*=>\s*“([^”]*)”'
import re
#解析城市编码和城市名称
def process_city_code(line:str,result:list):
    matchs = re.findall(pattern,line)
    result.append(
        {
        'city':matchs[0][0],
        'code':matchs[0][1]
        })
    return result
city_code=[]
try:
    with open(file_name,'r',encoding='utf-8') as f:
        for line in f:
            trim_line = line.strip()
            # 跳过空行和注释行
            if not trim_line or trim_line.startswith('#'):
                continue
            process_city_code(trim_line,city_code)
except Exception as e:
    print(f"处理文件时出错: {e}")

print(city_code)
