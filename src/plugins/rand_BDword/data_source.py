import httpx
import json
from random import choices

async def get_words():
    '''
    提取words的url
    '''
    # 推荐使用此方法
    # 调取爆点语录的链接api
    # async with httpx.AsyncClient() as client:
    #     resp = await client.get('https://my-json-server.typicode.com/sliefamily/bdg-bot/db')
    #     json_data = resp.json()['words']
    #     return choices(json_data,k-1)[0]
    # return None

    # 读取本地json文件
    with open('/home/bdg-bot/db.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)['words']
        return choices(json_data, k=1)[0]
    return None