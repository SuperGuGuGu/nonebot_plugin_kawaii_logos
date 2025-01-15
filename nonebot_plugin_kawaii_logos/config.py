from nonebot import get_plugin_config, logger
from pydantic import BaseModel
from pathlib import Path
from nonebot import require

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store


class Config(BaseModel):
    qbm_url: str
    qbm_username: str
    qbm_password: str
    qbm_enable_user: list[str] = []
    qbm_send_text: bool = False


menu_data = [
    {
        "trigger_method": "qb帮助",
        "func": "列出命令列表",
        "trigger_condition": " ",
        "brief_des": "qb帮助",
    }
]

plugin_config = get_plugin_config(Config)
# qb_url = plugin_config.qbm_url

plugin_cache_dir: Path = store.get_plugin_cache_dir()
# plugin_config_dir: Path = store.get_plugin_config_dir()
plugin_data_dir: Path = store.get_plugin_data_dir()
