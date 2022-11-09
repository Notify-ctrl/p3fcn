#!python

import sys

def main():
  infile = sys.argv[1]
  if infile == "":
    return
  f = open(infile, "rb")
  datas = f.read().split(b'TMX0')
  datas.remove(datas[0])
  for st in datas:
    st = st[24:52].decode().replace("\x00", "")
    print(st + ".tmx")

main()
