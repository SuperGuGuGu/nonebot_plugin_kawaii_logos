from PIL import Image
from .tools import circle_corner


async def template_1(logo_data: dict[str, str]) -> Image.Image:
    """
    模板1
    :param logo_data:
    :return:
    """
    image = Image.new("RGBA", (100, 100), "#FFFFFF")
    return image

