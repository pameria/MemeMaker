from PIL import Image, ImageDraw, ImageFont
import textwrap

im = Image.open("my.jpg")
draw = ImageDraw.Draw(im)
im_height, im_width = im.size
font = ImageFont.truetype(font="./impact/impact.ttf", size=int(im_height / 10))

top = input("Type in your Top Text: ")
bottom = input("Type in your Bottom Text: ")

top = top.upper()
bottom = bottom.upper()

char_h, char_w = font.getsize('A')
chars = im_width

top_lines = textwrap.wrap(top, width=chars)
bottom_lines = textwrap.wrap(bottom, width=chars)

y = 10
for line in top_lines:
    line_width, line_height = font.getsize(line)
    x = (im_width - line_width) / 2
    draw.text((x, y), line, fill='white', font=font)
    y += line_height

y = im_height - char_h * len(bottom_lines) - 15

for line in bottom_lines:
    line_width, line_height = font.getsize(line)
    x = (im_width - line_width) / 2
    draw.text((x, y), line, fill='black', font=font)
    y += line_height

im.show()
