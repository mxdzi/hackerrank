#!/usr/bin/env bash

i=1
while [[ $i -le 100 ]]; do
    if (($i % 2 == 1 ))
    then
        printf "$i\n"
    fi
    i=$((i+1))
done
