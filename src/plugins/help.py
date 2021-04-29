import nonebot
import json
from nonebot import on_command,on_regex,on_notice
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message,MessageSegment

async def get_keys():
    '''
    提取image库中所有关键词
    '''
    # 推荐使用此方法
    # 调取表情包链接api
    # async with httpx.AsyncClient() as client:
    #     resp = await client.get('https://my-json-server.typicode.com/sliefamily/bdg-bot/db')
    #     json_data = resp.json()['bqb']

    # 读取本地json文件
    with open('/home/bdg-bot/db.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)['bqb']
        return [i['key'] for i in json_data]
    return None

help_msg = """欢迎使用爆点Robot！
本机器人拥有的功能有：
----------
1.爆点语录
2.美图发送
3.BV/av号转小程序
4.网易云点歌（检修中）
5.考研倒计时（检修中）
6.群表情包
----------
你可以通过*/keys命令，查看详情"""
helper = on_command("*/help", aliases=set(['*/help','*/帮助']), priority=2)

@helper.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["queshi"] = args

@helper.got("queshi", prompt="help列表会很刷屏，你确定你想看？\n(回复：确实)")
async def handle_second_recevie(bot: Bot, event: Event, state: T_State):
    if state["queshi"] != "确实":
        await helper.reject("无效命令，吖屎啦")
    await helper.send(Message(help_msg))

@helper.got("keyCom")
async def keyLook(bot: Bot, event: Event, state: T_State):
    if state["keyCom"] != "*/keys":
        await helper.reject("无效命令，吖屎啦")
    keyList = await get_keys()
    msg_ = "可以用关键词.jpg触发图片发送，关键词列表如下：\n"
    for i in range(0,len(keyList)):
        msg_ += f"{i+1}. {keyList[i]}\n"
    await helper.send(Message(msg_))