#!python

import codecs
import struct
import sys

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
    ret = ret + decode_char(n)
    n = 0
  return ret

def getStrLen(fp):
  ret = 0
  in00 = False
  while True:
    temp = fp.read(1)
    if temp == b'':
      return ret
    if temp != b'\x00' and in00:
      return ret - 1
    ret = ret + 1
    if temp == b'\x00':
      in00 = True
  return ret

# seek point:
# 0x4D87E0
# 0x4D8C08
def main():
  args = sys.argv
  elf_file = open("SLPM_666.90", "rb+")
  translate = open(args[1], "rb")
  while True:
    data = translate.readline()
    if type(data) == str:
      break
    if data == b'' or data == b'\x00':
      break
    offset = int(data[7:len(data)].rstrip(), 16)
    translate.readline()
    data = translate.readline()
    target = data[7:len(data)].rstrip()
    target = target.replace(b'\\0', b'\0')
    target = target.decode()
    translate.readline()
    if target=="":
      continue
    elf_file.seek(offset)
    length = getStrLen(elf_file)
    print('%x, %s' % (offset, target))
    buf_target = b''
    for c in target:
      buf_target += encode_char(c)
    if len(buf_target) > length:
      return ValueError("超过长度（最大%d字节）：%s" % (length, target))
    else:
      elf_file.seek(offset)
      elf_file.write(buf_target)
      elf_file.write(b'\x00')


if __name__ == "__main__":
  main()