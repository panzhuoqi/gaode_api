# 路径规划
key_pan = 'your_key' #在这里输入你的key值
def walking(origin:str,destination:str)->dict:
    '''步行路径规划高德API'''
    url='https://restapi.amap.com/v3/direction/walking?parameters'
    param={
        'key':key_pan,
        'origin':origin,
        'destination':destination,
        'output':'json'
    }
    response = requests.get(url,params=param)
    data=response.json()
    return data
