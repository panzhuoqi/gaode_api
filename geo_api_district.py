# 行政区域查询
key_pan = 'your_key' #在这里输入你的key值
def district(keywords:str,destination:str)->dict:
    url='https://restapi.amap.com/v3/config/district?parameters'
    param={
        'key':key_pan,
        'keywords':keywords,
        'subdistrict':subdistrict,
        'output':'json'
    }
    response = requests.get(url,params=param)
    data=response.json()
    return data 
