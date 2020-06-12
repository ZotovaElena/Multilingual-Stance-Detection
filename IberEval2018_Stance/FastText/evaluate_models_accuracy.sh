#!/bin/sh

model=$1
gold_data=$2

./fasttext predict $model $gold_data | paste - $gold_data | awk ' { print $1"\t"$2 } ' | awk ' { if($1==$2) sum+=1 } END { print sum/NR } '
