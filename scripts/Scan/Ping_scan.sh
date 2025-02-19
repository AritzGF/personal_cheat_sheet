#!/bin/bash

red="192.168.25" 

for ip in {1..254}; do
    ping -c 1 -W 1 "$red.$ip" &>/dev/null && echo "Host activo: $red.$ip" &
done

wait

