#!bash

pe="wine /home/notify/Games/ps2/p3f汉化/PE-p3fimp/PersonaEditorCMD.exe"
pak="wine /home/notify/Games/ps2/p3f汉化/release/PAKPack.exe"

# 要导出的文件：PAK SPR BMD BF PM1

find -name "*.PM1" -exec $pe "{}" -expptp /sub /co2n \;
find -name "*.BF" -exec $pe "{}" -expptp /sub /co2n \;
find -name "*.PAK" -exec $pak unpack "{}" \;
find \( -name "*.SPR" -or -name "*.spr" \) -exec $pe "{}" -expall \;
find \( -name "*.BMD" -or -name "*.bmd" \) -exec $pe "{}" -expptp /sub /co2n \;
