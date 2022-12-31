#!/bin/python

import xml.etree.ElementTree as xml
import sys

font = xml.ElementTree(file = "./FONT0.xml").getroot()
lineno = 293

src_items = font.findall("./")
for i in range(1, lineno + 1):
  line = font.find("Line_" + str(i))
  if not line:
    line = xml.Element("Line_" + str(i))


  for j in range(1, 17):
    item = line.find("Glyph_" + str(j))
    if not item:
      item = xml.Element("Glyph_" + str(j))
      lc = xml.fromstring("<LeftCut>0</LeftCut>")
      lc2 = xml.fromstring("<RightCut>24</RightCut>")
      item.append(lc)
      item.append(lc2)
      line.append(item)

  l = font.find("Line_" + str(i))
  if l:
    font.remove(l)
  font.append(line)

x = xml.ElementTree()
x._setroot(font)
x.write("out.xml")

print(src_items[0])
