# 交通态势
key_pan = 'your_key' #在这里输入你的key值
def rectangle(rectangle:str)->dict:
    url='https://restapi.amap.com/v3/traffic/status/rectangle?parameters'
    param={
        'key':key_pan,
        'rectangle':rectangle,
        'output':'json'
    }
    response = requests.get(url,params=param)
    data=response.json()
    return data 
