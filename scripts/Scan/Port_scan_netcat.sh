#!/bin/bash

host="192.168.25.100"

for port in {1..1024}; do
    nc -z -v -w1 $host $port 2>&1 | grep "succeeded"
done

