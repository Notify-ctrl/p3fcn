#!/bin/python

# Python code to search .mp3 files in current
# folder (We can change file type/name and path
# according to the requirements.
import os
import re

err = False

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
                orig = secs[4]
                tr = secs[5]
                tr = tr.strip()
                if tr == "":
                #  print(fname, ":", lineno, ": 缺漏翻译")
                  continue
                reg = "\{[^\}]+\}"
                list1 = re.findall(reg, orig)
                list2 = re.findall(reg, tr)
                if ignore0a:
                  while list1.count("{0A}"):
                    list1.remove("{0A}")
                  while list2.count("{0A}"):
                    list2.remove("{0A}")
                if set(list1) != set(list2):
                  err = True
                  print(str(fname) + ":" + str(lineno), ": 原文和翻译控制符不同", list1, list2)
            if rewrite:
              fp = open(f, "w")
              fp.writelines(data)


if err:
    raise ValueError("Check Failed")
