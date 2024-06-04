#!/bin/bash
read n
read -a arr
mini=${arr[0]}
maxi=0
for((i=1;i<n;i++));
do
    if [ $mini -gt ${arr[i]} ]; then
    mini=${arr[i]}
    else
    if [ $maxi -lt $((${arr[i]}-$mini)) ]; then
    maxi=$((${arr[i]}-mini))
    fi
fi
done
echo "Maximum profit: $maxi"