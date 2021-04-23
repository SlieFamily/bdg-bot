import nonebot
import re
from .config import Config
from nonebot import on_command,on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message,MessageSegment

from .data_source import get_words,IsAdded

# 默认配置
global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

# 响应命令
BDwords = on_command("BDwords", aliases=set(['*/爆点语录','*/BD语录','*/bd语录']), priority=2)
Addwords = on_regex("\*/add (\w+) \*/end")

@BDwords.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    words = await get_words()
    await BDwords.finish(Message(words))


@Addwords.handle()
async def handle_first_receive(bot: Bot,event: Event, state: T_State):
    words = re.findall("\*/add (\w+) \*/end",str(event.get_message()))
    if IsAdded(words):
        await Addwords.finish("语录追加成功！爆点世界重构中~")
    else:
        await Addwords.finish("语录追加失败了，吖屎啦！")


