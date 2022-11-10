#!/bin/python

# Python code to search .mp3 files in current
# folder (We can change file type/name and path
# according to the requirements.
import os

dic = {}
dic2 = {}
fp = open("txt.TXT")
p3c = fp.read()
fp.close()
for c in p3c:
  if not c in dic:
    dic[c] = True
  else:
    if not c == "\n" and not c == " ":
      pass#print(c, end="")

# This is to get the directory that the program
# is currently running in.
dir_path = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk(dir_path):
    for file in files:

        # change the extension from '.mp3' to
        # the one of your choice.
        if file.endswith('.txt') or file.endswith('.TXT'):
            f = root+'/'+str(file)
            #print(f)
            fp=open(f)
            cnc = fp.read()
            fp.close()
            fname = f.replace(dir_path, "")
            fp = open(f)
            data = fp.readlines()
            fp.close()
            lineno = 0
            rewrite = False
            while True:
              lineno = lineno + 1
              if lineno > len(data):
                break
              cnc = data[lineno-1]
              secs = cnc.split('\t')
              if len(secs) < 6:
                # print(fname, ":", lineno, ": 缺漏翻译")
                pass
              else:
                cnc = secs[5]
                for c in cnc:
                  if not c in dic:
                    print(c, end = "")
                  #if not c in dic2:
                    dic[c] = True


'''
fp = open("5k.txt")
cnc = fp.read()
fp.close()

print()

for c in cnc:
  if not c in dic:
    print(c, end = "")
  if not c in dic2:
    dic2[c] = True

for c in p3c:
  if not c in dic2:
    pass#print(c, end = "")
    '''
