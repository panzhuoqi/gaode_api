# IP定位
key_pan = 'your_key' #在这里输入你的key值
def ip(keywords:str)->dict:
    url='https://restapi.amap.com/v3/ip?parameters'
    param={
        'key':key_pan,
        'output':'json'
    }
    response = requests.get(url,params=param)
    data=response.json()
    return data 
