import requests
import time
import json
from PIL import Image
import hitherdither
import numpy as np

headers = {
    'origin': 'https://pixelplanet.fun',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'lt,en-US;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'referer': 'https://pixelplanet.fun/',
    'authority': 'pixelplanet.fun',
    'cookie': '__cfduid=YOUR_COOKIE',
}

color_palette = [0xFFFFFF, 0xE4E4E4, 0x888888, 0x4E4E4E, 0x000000, 0xF3B5A8, 0xFFA5CE, 0xFF6267, 0xE20200, 0xFFA164,
                 0xE99400, 0x9D6D42, 0xF0DEB3, 0xE7D705, 0x9ADF37, 0x00C500, 0x006616, 0xCAE2FF, 0x00D5D1, 0x008BBC,
                 0x0001E3, 0x131D6C, 0xC872DD, 0x810274]


def place_pixel(pos_x, pos_y, color):
    a = pos_x + pos_y + 8

    data = '{"x":' + str(pos_x) + ',"y":' + str(pos_y) + \
           ',"color":' + str(color) + ',"fingerprint":"YOUR_FINGERPRINT","token":null,"a":' + str(
        a) + '}'
    try:
        response = requests.post('https://pixelplanet.fun/api/pixel', headers=headers, data=data)
        response_content = response.content.decode("utf-8")
        response_content = json.loads(response_content)
        successful = bool(response_content["success"])
        total_wait = float(response_content["waitSeconds"])
        more_to_wait = float(response_content["coolDownSeconds"])
    except:
        successful = False
        more_to_wait = 10
        total_wait = 10
    if total_wait > 0:
        time.sleep(total_wait)
    else:
        time.sleep(1)
        successful, more_to_wait, total_wait = place_pixel(pos_x, pos_y, color)
    return successful, more_to_wait, total_wait


def load_and_dither_image(image_path):
    img = Image.open(image_path)
    palette = hitherdither.palette.Palette(color_palette)
    img_dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(img, palette, order=8)
    # image_arr = np.asarray(img)
    image_arr = np.asarray(img_dithered) + 2
    # print(img_dithered)

    return image_arr


def draw_from_image(image_path, start, start_from=(0, 0)):
    start_x, start_y = start
    image = load_and_dither_image(image_path)
    for y_img, row in enumerate(image):
        if y_img < start_from[1]:
            continue
        for x_img, pixel in enumerate(row):
            if x_img < start_from[0] and y_img == start_from[1]:
                continue
            if pixel == 2:
                continue
            place_pixel(start_x + x_img, start_y + y_img, pixel)


if __name__ == '__main__':
    draw_from_image("Archlinux.png", (1000, -1000), (0, 0))
    # pos_x = 2767
    # pos_y = -13256
    # for i in range(25):
    #     place_pixel(pos_x + i, pos_y, 2 + i)
    #     time.sleep(1)
