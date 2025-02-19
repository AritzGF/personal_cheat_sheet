#!/bin/bash

host="192.168.25.100"
start_port=1
end_port=1024

for port in $(seq $start_port $end_port); do
    (echo > /dev/tcp/$host/$port) &>/dev/null && echo "Puerto $port abierto"
done
