#!/bin/bash
while read line; do
    arr=()
    read -a arr <<< $line
    length=${#arr[@]}
    j=$((length-1))
    for((i=0; i<length && j>=i;));
    do
        if [ "${arr[i]}" == "#" ] || [ "${arr[i]}" == "*" ] || [ "${arr[i]}" == "$" ] || [ "${arr[i]}" == "@" ] ;
        then
            i=$((i+1))
            continue
        elif [ "${arr[j]}" == "#" ] || [ "${arr[j]}" == "*" ] || [ "${arr[j]}" == "$" ] || [ "${arr[j]}" == "@" ] ;
        then
            j=$((j-1))
        else
            temp="${arr[i]}"
            arr[i]="${arr[j]}"
            arr[j]="$temp"
            i=$((i+1))
            j=$((j-1))
        fi
    done
    echo "${arr[@]}"
    unset arr
done <$1


