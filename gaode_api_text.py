# 搜索POI
key_pan = 'your_key' #在这里输入你的key值
def text(keywords:str)->dict:
    url='https://restapi.amap.com/v3/place/text?parameters'
    param={
        'key':key_pan,
        'keywords':keywords,
        'output':'json'
    }
    response = requests.get(url,params=param)
    data=response.json()
    return data 
