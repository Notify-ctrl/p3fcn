#!python

import codecs
import struct

font_map_dict = {}
font_map = open("P4.FNTMAP", "rb")
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
  if n >= 0 and n < len(font_map_dict):
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
    elif n == 0:
      break
    else:
      i = i + 1
    dec = decode_char(n)
    if dec == "":
      if n > 0x80:
        dec = "{%X}" % (buf[i - 1] + buf[i - 2] * 0x100)
      else:
        dec = "{%X}" % n
    ret = ret + dec
    n = 0
  return ret

def readAString(fp):
  ret = b''
  while True:
    temp = fp.read(1)
    if temp == b'':
      return ''
    ret = ret + temp
    if temp == b'\x00':
      break
  return ret

# seek point:
# 0x4D87E0
# 0x4D8C08
def main():
  elf_file = open("SLPM_666.90", "rb")
  out = open("out.txt", "w")
  while True:
    data = readAString(elf_file)
    if type(data) == str:
      break
    if data == b'' or data == b'\x00':
      continue
    out.write("offset=0x%X\n" % (elf_file.tell() - len(data)))
    out.write("original=%s\n" % handleBuffer(data))
    out.write("target=\n------\n")


if __name__ == "__main__":
  main()