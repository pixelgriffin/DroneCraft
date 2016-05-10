#!/bin/bash
for i in $(seq 1 1 500)
do
	./Release/DroneCraft 14,10,60,13,10,3,2,22,14,4,7,1 $i >> $1
done
