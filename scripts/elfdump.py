#!python

import codecs

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
  pass

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
'''
# 00 - 21byte
txt_file = open("MSG(00).DAT", "rb")
out_file = open("MSG(00).TXT", "w")
while True:
  buf = txt_file.read(21)
  if buf == b'':
    break
  out_file.write(handleBuffer(buf) + "\n")

# MSG(01).DAT
# 每一项19字节。
txt_file = open("MSG(01).DAT", "rb")
out_file = open("MSG(01).TXT", "w")
while True:
  buf = txt_file.read(19)
  if buf == b'':
    break
  out_file.write(handleBuffer(buf) + "\n")

# 02.dat
# 19
txt_file = open("MSG(02).DAT", "rb")
out_file = open("MSG(02).TXT", "w")
while True:
  buf = txt_file.read(19)
  if buf == b'':
    break
  out_file.write(handleBuffer(buf) + "\n")

# 03.dat
# 17
txt_file = open("MSG(03).DAT", "rb")
out_file = open("MSG(03).TXT", "w")
while True:
  buf = txt_file.read(17)
  if buf == b'':
    break
  out_file.write(handleBuffer(buf) + "\n")
'''

txt_file=open("SLPM_666.90","rb")
out_file=open("1.txt","w")
buf=txt_file.read()
out_file.write(handleBuffer(buf))
