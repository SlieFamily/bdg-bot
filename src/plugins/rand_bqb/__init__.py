import nonebot
from .config import Config
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message,MessageSegment

from .data_source import Get_image

# 默认配置
global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

# 响应命令
group_bqb = on_command("group_bqb", aliases=set(['*群表情包', '*yj语录', '*经典语录', '*断章取义']), rule=to_me(), priority=1)

@group_bqb.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 获取指令后的key
    if args:
        state["key"] = args  # 若有则直接赋值

@group_bqb.got("key",prompt="请输入<断章取义>的关键词")
async def handle_key(bot: Bot, event: Event, state: T_State):
    key = state["key"]
    # 此处插入关键词匹配代码
    # if key not in ["上海", "北京"]:
        # await group_bqb.reject("你想查询的城市暂不支持，请重新输入！")
    
    key_image_url = await get_image(key)
    await group_bqb.finish(MessageSegment.image(key_image_url))





