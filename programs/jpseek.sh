#!/bin/sh

cd $3/programs
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:. ./jpseek $1 $2
chmod 666 $2
