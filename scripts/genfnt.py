#!/bin/python

import os
from PIL import Image

from fontTools.ttLib import TTFont
#fontType = "/home/notify/.fonts/汉/汉仪文黑_85W.ttf"
fontType = "/home/notify/.fonts/h/HYRuiHuSongW.ttf"

hywh = TTFont(fontType)
hywhMap = hywh['cmap'].tables[0].ttFont.getBestCmap()

skip = TTFont("/home/notify/.fonts/s/Skip_EB.otf")
skipMap = skip['cmap'].tables[0].ttFont.getBestCmap()

os.system("rm out.png out2.png")
os.system("convert -size 512x32 xc:black tmp.png")

fp = open("自用字库/orig-nomap.txt")
content = fp.read()
fp.close()
total = len(content)
cur = 0

pic_row = 29
row = 0
column = 0

for char in content:
  cur = cur + 1
  if not char == "\n":
    x = 3 + 32 * column
    y = 24
    if char == "\"":
      char = "\\\""
    elif char == "`":
      char = "\\`"
    elif char == "\0":
      char = " "
    txtBody = F"\"text {x},{y} '{char}'\""
    #font = "'/home/notify/.fonts/造/造字工房典黑（非商用）常规体.ttf'"
    #font = "\"HYWenHei-85W-Heavy\""
    font = "HYRuiHuSong"
    if len(char) == 1 and not ord(char) in hywhMap.keys():
      font="Skip-EB"
      if not ord(char) in skipMap.keys():
        font="SimHei"
    command = F"convert -family {font} -fill white -pointsize 28 -weight ExtraBold -draw {txtBody} tmp.png tmp.png >/dev/null 2>&1"
    os.system(command)
    prog = int(cur / total * 32)
    print("\r" + "[" + "#" * prog + "." * (32 - prog) + f"][{cur}/{total}]", end = "")
    column = column + 1
  else:
    row = row + 1
    column = 0
    os.system("convert tmp.png -resize 512x26! tmp.png")
    os.system("convert tmp.png -resize 512x32 -background black -gravity center -extent 512x32 tmp.png")
    os.system("if [ ! -e out2.png ]; then cp tmp.png out2.png; else convert -append out2.png tmp.png out2.png; fi")
    if row % 16 == 0:
      os.system("convert -append out.png out2.png out.png")
      os.system("rm out2.png")
    os.system("convert -size 512x32 xc:black tmp.png")

os.system("if [ ! -e out.png ]; then cp out2.png out.png; else convert -append out.png out2.png out.png; fi")
os.system("rm out2.png")
