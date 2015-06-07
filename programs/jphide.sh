#!/bin/bash

cd $4/programs
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:. ./jphide $1 $2 $3
