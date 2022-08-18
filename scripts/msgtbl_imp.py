#!python

import codecs
import struct

'''
0x00~0x7F: ascii
0x80~0x4F + 0x80~0xFF: char

let n = 0x814F
index of n = (0x81-0x80) * 0x80(128) + 0x4F
        + 32 (ASCII 0x00-0x20 is not used)

so encode char is:
1. find index of the char in the font_map_dict
2. if index = n:
    let low16bit = n % 0x80 + 0x80
    let high16bit = n / 0x80 + 0x80
'''

font_map_dict = {}
font_map = open("/home/notify/Games/ps2/p3f汉化/PE-p3fimp/font/P4.FNTMAP", "rb")
i = 0
while True:
  buf = font_map.read(2)
  if buf == b'':
    break
  font_map_dict[i] = codecs.utf_16_le_decode(buf)[0]
  i = i + 1

def encode_char(c):
  if ord(c) < 0x80:
    return struct.pack("B", ord(c))
  index = list(font_map_dict.keys())[list(font_map_dict.values()).index(c)]
  index = index - 32
  l16b = index % 0x80 + 0x80
  h16b = int(index / 0x80) + 0x80
  a=l16b + h16b * 0x100
  return struct.pack(">H",a)

def decode_char(n):
  if n >= 0 and n < 0x1670:
    return font_map_dict[n]
  return ""

def handleBuffer(buf):
  n = 0
  i = 0
  ret = ""
  while i < len(buf):
    n = buf[i]
    if n >= 0x80:
      # n = (n << 8) | buf[i+1]
      n = (n - 0x81) * 128 + buf[i + 1] + 32
      i = i + 2
    #elif n == 0:
    #  break
    else:
      i = i + 1
    ret = ret + decode_char(n)
    n = 0
  return ret

# readline, then write to binfile
# if line empty, ret

# 00 - 21byte
txt_file = open("MSG(00).TXT", "r")
out_file = open("MSG(00).DAT", "wb")
while True:
  line = txt_file.readline()
  line = line[:-1]
  if line == '':
    break
  rest = 21
  for char in line:
    tx = encode_char(char)
    out_file.write(tx)
    rest = rest - len(tx)
  for i in range(0, rest):
    out_file.write(b'\x00')

# MSG(01).DAT
# 每一项19字节。
txt_file = open("MSG(01).TXT", "r")
out_file = open("MSG(01).DAT", "wb")
while True:
  line = txt_file.readline()
  line = line[:-1]
  if line == '':
    break
  rest = 19
  for char in line:
    tx = encode_char(char)
    out_file.write(tx)
    rest = rest - len(tx)
  for i in range(0, rest):
    out_file.write(b'\x00')

# 02.dat
# 19
txt_file = open("MSG(02).TXT", "r")
out_file = open("MSG(02).DAT", "wb")
while True:
  line = txt_file.readline()
  line = line[:-1]
  if line == '':
    break
  rest = 19
  for char in line:
    tx = encode_char(char)
    out_file.write(tx)
    rest = rest - len(tx)
  for i in range(0, rest):
    out_file.write(b'\x00')

# 03.dat
# 17
txt_file = open("MSG(03).TXT", "r")
out_file = open("MSG(03).DAT", "wb")
while True:
  line = txt_file.readline()
  line = line[:-1]
  if line == '':
    break
  rest = 17
  for char in line:
    tx = encode_char(char)
    out_file.write(tx)
    rest = rest - len(tx)
  for i in range(0, rest):
    out_file.write(b'\x00')

'''
txt_file=open("SLPM_666.90","rb")
out_file=open("1.txt","w")
buf=txt_file.read()
out_file.write(handleBuffer(buf))
'''

