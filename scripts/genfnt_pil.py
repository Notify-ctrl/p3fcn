#!/bin/python

import os
import math
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

hywh = TTFont("/home/notify/.fonts/h/HYRuiHuSongW.ttf")
hywhMap = hywh['cmap'].tables[0].ttFont.getBestCmap()

skip = TTFont("/home/notify/.fonts/s/Skip_EB.otf")
skipMap = skip['cmap'].tables[0].ttFont.getBestCmap()

simhei = TTFont("/usr/share/fonts/noto-cjk/NotoSansCJK-Bold.ttc", fontNumber=0)
simheiMap = simhei['cmap'].tables[0].ttFont.getBestCmap()

hywh = ImageFont.truetype("/home/notify/.fonts/h/HYRuiHuSongW.ttf", 24)
skip = ImageFont.truetype("/home/notify/.fonts/s/Skip_EB.otf", 24)
simhei = ImageFont.truetype("/usr/share/fonts/noto-cjk/NotoSansCJK-Bold.ttc", 24)

def getFallbackFont(char):
  font = hywh
  if (char == "佉"):
    return simhei
  if len(char) == 1 and not ord(char) in hywhMap.keys():
    font = skip
    if not ord(char) in skipMap.keys():
      font = simhei
      if not ord(char) in simheiMap.keys():
        print("字体库缺少汉字：", char)
  return font

fp = open(os.path.dirname(os.path.realpath(__file__)) + "/../CVM/txt.TXT")
content = fp.read()
fp.close()
total = len(content)
cur = 0

out = Image.new('RGB', (512, math.ceil(total / 16) * 32 - 64))
orig_font = Image.open(os.path.dirname(os.path.realpath(__file__)) + "/font.png").convert('RGBA')
out.paste(orig_font, (0, 0), orig_font)

for char in content:
  cur = cur + 1
  print("\r[" + str(cur) + "/" + str(total) + "]", end = "")
  if cur < 480 or char == "\0" or char == " ":
    continue

  x = 32 * ((cur - 32 - 1) % 16)
  y = 32 * math.floor((cur -  32 - 1) / 16) + 3

  tmpimage = Image.new('RGB', (32, 32))
  painter = ImageDraw.Draw(tmpimage)
  fallbackfont = getFallbackFont(char)
  fallbacky = -1
  if fallbackfont == skip:
    fallbacky = 4
  elif fallbackfont == simhei:
    fallbacky = -4

  painter.text((0, fallbacky), char, (255, 255, 255), fallbackfont)
  tmpimage = tmpimage.resize((32, 26))
  out.paste(tmpimage, (x, y))

out.save("out.png", format = "png")
