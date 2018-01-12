#!/usr/bin/env bash



# store arguments from bash command line in special array
args=("$@")

# SEQ holds the number of arguments passed in
SEQ=$#

declare -i sizeA=$#

declare ARGS_ARRAY[sizeA]

# echo each element in array
# for loop
for (( i=0;i<$SEQ;i++)); do
    #  every second arg = value - use the first as the index value
    n=$((i%2))
    if [ $n -eq 0 ]; then
        v=i+1
        INDEX=${args[${i}]}
        VALUE=${args[${v}]}
        ARGS_ARRAY[$INDEX]=$VALUE
        echo "pling: " $INDEX "," ${ARGS_ARRAY[$INDEX]}
    fi
done
