#!bash

pe="wine /home/notify/Games/ps2/p3f汉化/PE-p3fimp/PersonaEditorCMD.exe"
pak="wine /home/notify/Games/ps2/p3f汉化/release/PAKPack.exe"

# 要导入的文件：PAK SPR BMD BF PM1 PTP TMX

find -name "*.TXT" -exec sed -i 's/；//g' "{}" \;

for f in `find -name '*.PTP'`
do
  fp=${f%.PTP}
  $pe $f -imptext ${fp}.TXT /map "%FN %MSGIND %STRIND %I %I %NEWSTR" /skipempty -save
done

find -name "*.PM1" -exec $pe "{}" -impptp /sub -save \;
find -name "*.BF" -exec $pe "{}" -impptp /sub -save \;
find \( -name "*.BMD" -or -name "*.bmd" \) -exec $pe "{}" -impptp /sub -save \;
find \( -name "*.TMX" -or -name "*.tmx" \) -exec $pe "{}" -impimage -save \;

for f in `find -name '*(NEW)*'`
do
  mv $f ${f/\(NEW\)/} -f
done

find \( -name "*.SPR" -or -name "*.spr" \) -exec $pe "{}" -impall -save \;

for f in `find -name '*(NEW)*'`
do
  mv $f ${f/\(NEW\)/} -f
done

find -name "*.PNG" -delete
find -name "*.PTP" -delete
find -name "*.TXT" -delete
for f in `find -name '*.spr'`; do
  for ff in `./spr.py $f`; do
    rm ${f%/*}/${ff}
  done
done

for f in `find -name '*.PAK'`
do
  fp=${f%.PAK}
  $pak replace $f $fp
  rm -rf $fp
done

