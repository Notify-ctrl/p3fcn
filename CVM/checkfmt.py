#!/bin/python

# Python code to search .mp3 files in current
# folder (We can change file type/name and path
# according to the requirements.
import os
import re

# This is to get the directory that the program
# is currently running in.
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/DATA"

for root, dirs, files in os.walk(dir_path):
    ignore0a = True
    for file in files:
        # change the extension from '.mp3' to
        # the one of your choice.
        if file.endswith('.txt') or file.endswith('.TXT'):
            f = root + '/' + str(file)
            #print(f)
            fname = f.replace(dir_path, "")
            fp = open(f)
            lineno = 0
            while True:
              cnc = fp.readline()
              lineno = lineno + 1
              if cnc == '':
                break
              secs = cnc.split('\t')
              if len(secs) < 6:
                print(fname, "\t- Line", lineno, ": 缺漏翻译")
              else:
                orig = secs[4]
                tr = secs[5]
                reg = "\{[^\}]+\}"
                list1 = re.findall(reg, orig)
                list2 = re.findall(reg, tr)
                if ignore0a:
                  while list1.count("{0A}"):
                    list1.remove("{0A}")
                  while list2.count("{0A}"):
                    list2.remove("{0A}")
                if set(list1) != set(list2):
                  print(fname, "\t- Line", lineno, ": 原文和翻译控制符不同", list1, list2)
            fp.close()

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
