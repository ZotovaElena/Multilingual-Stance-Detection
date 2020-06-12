cat $1 | perl -pe 's/__label__//g' | perl -pe 's/NEUTRAL/NONE/g' | awk ' { print "0\tjar\tjar\t"$1 } '
