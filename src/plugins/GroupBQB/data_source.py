import httpx
import json

async def get_image(key:str):
    '''
    根据关键词提取image的url
    '''
    # 推荐使用此方法
    # 调取表情包链接api
    # async with httpx.AsyncClient() as client:
    #     resp = await client.get('https://my-json-server.typicode.com/sliefamily/bdg-bot/db')
    #     json_data = resp.json()['bqb']

    # 读取本地json文件
    with open('/home/bdg-bot/db.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)['bqb']
        
    for i in range(0,len(json_data)):
        if json_data[i]["key"] == key:
            return json_data[i]["url"]
    return None