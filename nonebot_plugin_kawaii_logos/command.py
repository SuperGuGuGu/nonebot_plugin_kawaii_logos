from nonebot import logger
from .draw import template_1


async def command_kawaii_logos(args: str):
    logo_data: dict = {}

    image = await template_1(logo_data=logo_data)

    return image

