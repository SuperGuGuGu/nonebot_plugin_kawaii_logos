# coding=utf-8
from nonebot import logger
from .draw import template_1


async def command_kawaii_logos(args: str):
    # 解析
    logo_data: dict = {
        "标题": "あアいイうウ",
        "副标题": "あアいイう",
        "下": "text",
        "上": "text",
    }
    # 检查内容长度
    if not 3 <= len(logo_data["标题"]):
        return "第1段文字过短"
    if not len(logo_data["标题"]) <= 10:
        return "第1段文字过长"
    if not 3 <= len(logo_data["副标题"]):
        return "第2段文字过短"
    if not len(logo_data["副标题"]) <= 10:
        return "第2段文字过长"
    if not 3 <= len(logo_data["下"]):
        return "第3段文字过短"
    if not len(logo_data["下"]) <= 15:
        return "第3段文字过长"
    if not 3 <= len(logo_data["上"]):
        return "第4段文字过短"
    if not len(logo_data["上"]) <= 15:
        return "第4段文字过长"

    image = await template_1(logo_data=logo_data)

    return image

