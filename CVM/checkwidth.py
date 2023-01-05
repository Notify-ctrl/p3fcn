#!/bin/python

import os
import re

err = False

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/DATA"

for root, dirs, files in os.walk(dir_path):
  ignore0a = True
  punc = ["。", "?", "？", "!", "！", ",", "，", "…", "⋯"]
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
      while True:
        lineno = lineno + 1
        if lineno > len(data):
          break
        cnc = data[lineno-1]
        secs = cnc.split('\t')
        if len(secs) < 6:
          pass
        else:
          orig = secs[4]
          tr = secs[5]
          tr = tr.strip()
          if tr == "":
            continue

          tr.removeprefix(";")
          tr.removeprefix("；")

          reg = "\{[^\}]+\}"

          trlist = tr.split("{0A}")
          for substr in trlist:
            extralen = 0
            relist = re.findall(reg, substr)

            for subreg in relist:
              substr = substr.replace(subreg, '')
              if subreg == '{F1 0A}' or subreg == '{F1 0B}':
                extralen += 3

            if len(substr) > 1 and substr[len(substr) - 1] in punc:
              extralen -= 1

            if len(substr) + extralen > 24:
              err = True
              print(str(fname) + ":" + str(lineno) + ": 宽度超24字符")


if err:
    raise ValueError("Check Failed")
