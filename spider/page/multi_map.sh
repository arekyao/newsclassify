#!/bin/bash

tmp="tmp"
log_tmp="log.tmp"

mkdir -p $tmp $log_tmp

ls db.page/ > list

awk -F "\t" '{if (FILENAME==ARGV[1]){
    flag[$0]=1;
}else{
    if (flag[$1]!=1){
        print $0;
    }
}
}' list $1 > $1".tmp"




rm -f $tmp/item_map_*
rm -f $log_tmp/item_map_*.log

split -l$2 -a3 $1".tmp" "item_map_"

mv item_map_* $tmp 

for i in `ls $tmp/item_map_*`;do
    echo $i
    python page_crawler.py $i > "log."$i".log" & 
done






