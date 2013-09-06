#!/bin/bash

ps ax |grep page_craw > sid

awk '{print $1}' sid > sid.tmp

for i in `cat sid.tmp`;do
    echo $i
    kill $i
done

rm sid sid.tmp

