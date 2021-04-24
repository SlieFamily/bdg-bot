import httpx
import json
from random import choices

def get_json():
    '''
    提取words的json内容
    '''
    # 推荐使用此方法
    # 调取爆点语录的链接api
    # async with httpx.AsyncClient() as client:
    #     resp = await client.get('https://my-json-server.typicode.com/sliefamily/bdg-bot/db')
    #     json_data = resp.json()

    # 这里是直接读取本地文件的方法
    with open('/home/bdg-bot/db.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)
        return json_data
    return None

async def get_words():
    '''
    提取words
    '''
    try:
        words = get_json()['BDwords']
        return choices(words,k=1)[0]
    except:
        return "发送失败，数据库维护中……"

def IsAdded(words):
    '''
    追加爆点语录
    '''
    json_data = get_json()
    json_data['BDwords'].append(words[0])
    with open("/home/bdg-bot/db.json", "w", encoding="utf8") as fp:
        json.dump(json_data, fp,ensure_ascii=False)
        print
        return True
    return False

def IsDel():
    '''
    删除上一条添加的语句
    '''
    json_data = get_json()
    del_msg = json_data['BDwords'].pop()
    with open("/home/bdg-bot/db.json", "w", encoding="utf8") as fp:
        json.dump(json_data, fp,ensure_ascii=False)
        print
        return del_msg
    return False