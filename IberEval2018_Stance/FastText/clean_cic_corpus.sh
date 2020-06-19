#!bin/sh

cat $1 | perl -pe 's/\r//g' | awk -F"\t" ' { print $NF"\t"$2 } ' | perl -pe 's/https?\S+//g' | sed 's/[[:punct:]]//g' | perl -pe 's/^NEUTRAL/NONE/g' | perl -pe 's/(AGAINST|FAVOR|NONE)\t/__label__\1\t/g'
