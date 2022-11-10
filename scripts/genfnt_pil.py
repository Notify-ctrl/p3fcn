#!/bin/python

import os
import math
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

hywh = TTFont("/home/notify/.fonts/h/HYRuiHuSongW.ttf")
hywhMap = hywh['cmap'].tables[0].ttFont.getBestCmap()

skip = TTFont("/home/notify/.fonts/s/Skip_EB.otf")
skipMap = skip['cmap'].tables[0].ttFont.getBestCmap()

hywh = ImageFont.truetype("/home/notify/.fonts/h/HYRuiHuSongW.ttf", 28)
skip = ImageFont.truetype("/home/notify/.fonts/s/Skip_EB.otf", 28)
simhei = ImageFont.truetype("/home/notify/.fonts/s/simhei.ttf", 28)

def getFallbackFont(char):
  font = hywh
  if len(char) == 1 and not ord(char) in hywhMap.keys():
    font = skip
    if not ord(char) in skipMap.keys():
      font = simhei
  return font

fp = open(os.path.dirname(os.path.realpath(__file__)) + "/../CVM/txt.TXT")
content = fp.read()
fp.close()
total = len(content)
cur = 0

out = Image.new('RGBA', (512, math.ceil(total / 16) * 32))

for char in content:
  cur = cur + 1
  print("\r[" + str(cur) + "/" + str(total) + "]", end = "")
  if cur < 480 or char == "\0" or char == " ":
    continue

  x = 32 * (cur % 16) + 3
  y = 32 * math.floor(cur / 16)

  tmpimage = Image.new('RGBA', (32, 32))
  painter = ImageDraw.Draw(tmpimage)
  painter.text((0, 0), char, (255, 255, 255), getFallbackFont(char))
  tmpimage = tmpimage.resize((32, 26))
  out.paste(tmpimage, (x, y), tmpimage)

out.save("out.png", format = "png")
