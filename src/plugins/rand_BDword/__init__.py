import nonebot
import re
from .config import Config
from nonebot import on_command,on_regex,on_notice
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message,MessageSegment,GroupIncreaseNoticeEvent

from .data_source import get_words,IsAdded,IsDel

# 默认配置
global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

# 响应命令
BDwords = on_command("BDwords", aliases=set(['爆点语录','BD语录','bd语录']), priority=2)
Addwords = on_regex("\+%([\s\S]+)%")
Delwords = on_command("-del",priority=2)
welcom = on_notice()
suanle = on_regex("算了|bdg|爆点哥|BDG")

@BDwords.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    words = await get_words()
    await BDwords.finish(Message(words))


@Addwords.handle()
async def handle_first_receive(bot: Bot,event: Event, state: T_State):
    words = re.findall("\+%([\s\S]*)%",str(event.get_message()))
    if IsAdded(words):
        await Addwords.finish(Message("语录追加成功，爆点世界重构中……"))
    else:
        await Addwords.finish(Message("追加失败了，吖屎啦！"))

@Delwords.handle()
async def handle_first_receive(bot: Bot,event: Event, state: T_State):
    if event.get_user_id() != "1364374624":
        await Delwords.finish(Message("你就是逊啊，没权限"))
    del_msg = IsDel()
    if del_msg:
        await Delwords.finish(Message("已将语录：\n-------\n"+del_msg+"\n-------\n删除！"))
    else:
        await Delwords.finish(Message("删除失败了，嗯嘿嘿"))

@welcom.handle()
async def handle_first_receive(bot: Bot,event: GroupIncreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    # msg = at_+'新人，想学爆点吗？'
    msg = at_+'欢迎新人进裙'
    await welcom.finish(Message(msg))

@suanle.handle()
async def handle_first_receive(bot: Bot,event: Event, state: T_State):
    await suanle.finish(Message("要算卦了？"))