#!/usr/bin/env bash

read n

if [[ $n = "Y" ]] || [[ $n = "y" ]]
then
    printf "YES"
elif [[ $n = "N" ]] || [[ $n = "n" ]]
then
    printf "NO"
fi
