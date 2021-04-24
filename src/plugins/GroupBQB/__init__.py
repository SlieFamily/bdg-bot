import nonebot
import re
from .config import Config
from nonebot import on_command,on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message,MessageSegment

from .data_source import get_image

# 默认配置
global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

# 响应命令
group_bqb = on_regex("([\S]+).jpg")

@group_bqb.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    key = re.findall("([\S]+).jpg",str(event.get_message()))[0]
    print(key)
    key_image_url = await get_image(key)
    if key_image_url:
        await group_bqb.finish(MessageSegment.image(key_image_url))
