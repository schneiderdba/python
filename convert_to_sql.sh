#!/bin/bash

while read line; do 

first=`echo $line |awk -F, '{print $1}' |tr -d "\""`
second=`echo $line |awk -F, '{print $2}'`
third=`echo $line |awk -F, '{print $3}' |tr -d "\""`
echo "INSERT INTO shopify (title, popularity, price) VALUES ('$first', $second, $third);"


done < file
