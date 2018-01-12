#!/bin/bash
# https://linuxconfig.org/bash-scripting-tutorial
# store arguments from bash command line in special array
args=("$@")

# SEQ holds the number of arguments passed in
SEQ=$#
declare -i sizeA=$#

case "$OSTYPE" in
  solaris*) echo "SOLARIS" ;;
  darwin*)  echo "OSX";echo "bing";declare ARGS_ARRAY[sizeA] ;;
  linux*)   echo "LINUX" declare -g -A ARGS_ARRAY;;
  bsd*)     echo "BSD" ;;
  msys*)    echo "WINDOWS" ;;
  *)        echo "unknown: $OSTYPE" ;;
esac


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
