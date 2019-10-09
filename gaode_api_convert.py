# 坐标转换
key_pan = 'your_key' #在这里输入你的key值
def convert(locations:str)->dict:
    url='https://restapi.amap.com/v3/assistant/coordinate/convert?parameters'
    param={
        'key':key_pan,
        'locations':locations,
        'output':'json'
    }
    response = requests.get(url,params=param)
    data=response.json()
    return data 
