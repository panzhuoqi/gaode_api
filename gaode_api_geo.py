#地理编码 
key_pan = 'your_key'  #在这里输入你的key值
def geo(add:str,city:str)->dict:
    '''获取地理编码'''
    url='https://restapi.amap.com/v3/geocode/geo?parameters'
    param={  
        'key':key_pan,
        'address':add,
        'city':city,
        'output':'json'
    }
    response = requests.get(url,params=param)
    data=response.json()
    return data 
