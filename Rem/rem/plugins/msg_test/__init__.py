from pathlib import Path
import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message

global_config = get_driver().config
config = Config.parse_obj(global_config)

day_anime = on_keyword({'小小红'})
@day_anime.handle()
async def _():
    await day_anime.finish(Message("喝酒了？喝酒了？"))





_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").resolve()))

