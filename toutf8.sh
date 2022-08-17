#!bash

for l in `find -name '*.txt' -or -name '*.TXT'`; do 
  if file -i $l | grep utf-16le; then
    iconv -f UTF16LE -t UTF-8//TRANSLIT $l -o $l
  fi
done
