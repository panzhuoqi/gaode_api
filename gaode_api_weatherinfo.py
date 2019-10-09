# 天气查询
key_pan = 'your_key' #在这里输入你的key值
def weatherInfo(city:str)->dict:
    url='https://restapi.amap.com/v3/weather/weatherInfo?parameters'
    param={
        'key':key_pan,
        'city':city,
        'output':'json'
    }
    response = requests.get(url,params=param)
    data=response.json()
    return data 
