#!/bin/bash
for fl in *.csv; do
mv $fl $fl.old
sed 's/FINDSTRING/REPLACESTRING/g' $fl.old > $fl
#rm -f $fl.old
done
