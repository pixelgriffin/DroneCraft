#!/bin/bash
for i in $(seq 1 1 500)
do
	./Release/DroneCraft 12,9,55,27,9,2,6,21,10,6,5,7 $i >> $1
done
