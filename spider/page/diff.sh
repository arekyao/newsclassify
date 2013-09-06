#!/bin/bash

if [ $# -ne 2 ];then
	echo "Usage: $0 f1 f2"
	exit
fi

awk -F "\t" '{if (FILENAME==ARGV[1]){
		flag[$0]=1;
	}else{
		if (flag[$1]==1){
			print $0;
		}
	}
}' $1 $2







