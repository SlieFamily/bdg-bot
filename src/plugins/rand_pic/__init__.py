import nonebot
from .config import Config
import httpx
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message,MessageSegment
from nonebot.log import logger


global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

setu = on_command("setu", aliases=set(['涩图', '色图', '来张色图', '来张涩图']), priority=1)

@setu.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://api.mtyqx.cn/api/random.php?return=json')
        logger.debug(resp.json())
        imgurl = resp.json()['imgurl']
        # cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
        await setu.send(MessageSegment.image(imgurl))





