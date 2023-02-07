#!/bin/bash

./elf_import.py elf_text.txt
for f in elf/*txt; do
  ./elf_import.py $f
done
