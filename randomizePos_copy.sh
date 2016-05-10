#!/bin/bash
for i in $(seq 1 1 500)
do
	./Release/DroneCraft_copy 18,8,63,18,16,1,1,8,13,4,5,3 $i >> $1
done
