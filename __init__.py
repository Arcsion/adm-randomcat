from nonebot import get_driver
from nonebot import on_command
from .config import Config
from nonebot.log import logger
import os
import random
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, Event

global_config = get_driver().config
config = Config.parse_obj(global_config)

rdcat = on_command("随机猫猫", priority=5, block=True)

@rdcat.handle()
async def _(bot: Bot, event: MessageEvent):
    pass
    rootdir = "C:\\qqbot\\res\\imglib\\猫猫" # 本地猫猫图库路径
    file_names = []
    for parent, dirnames, filenames in os.walk(rootdir):
        file_names = filenames 
    x = random.randint(0, len(file_names)-1)
    # print(file_names[x])
    image_file = f"file:///C:/qqbot/res/imglib/猫猫/{file_names[x]}"
    msg = f"[CQ:image,file={image_file}]"
    try:
        logger.info(f"[RandomCat]Will send cat gif {file_names[x]}.")
        await bot.send_group_msg(group_id=event.group_id, message=msg)
    except Exception as e:
        logger.info(e)