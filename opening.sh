#!/bin/sh

clip=`xclip -o -selection clipboard`
echo $clip
/home/mononoke/Desktop/scripts/auto-type/env/bin/python ~/Desktop/scripts/auto-type/code/script2.py $clip