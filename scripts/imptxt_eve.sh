#!/bin/bash

pe="wine /home/notify/Games/ps2/p3f汉化/PE-p3fimp/PersonaEditorCMD.exe"

for f in `find -name "*.PM1"`
do
  fp=${f%.PM1}
  $pe $f -expptp /sub /co2n
  $pe ${fp}.PTP -imptext ${fp}.TXT /map "%FN %MSGIND %STRIND %I %I %NEWSTR" /skipempty -save
  $pe $f -impptp /sub -save
  rm ${fp}.PTP
done

