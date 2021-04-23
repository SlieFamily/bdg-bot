import nonebot
from .config import Config
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message,MessageSegment

from .data_source import get_words

# 默认配置
global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

# 响应命令
BDwords = on_command("BDwords", aliases=set(['*/爆点语录','*/BD语录','*/bd语录']), priority=2)
Addwords = on_regex("*/add []")

@BDwords.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    words = await get_words()
    await BDwords.finish(Message(words))





