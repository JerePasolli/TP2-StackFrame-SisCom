#!/bin/bash

if [ -d "build" ]; then
    rm -rf ./build
    mkdir ./build
else
    mkdir ./build
fi

nasm -f elf32 src/add_one.asm -o build/add_one.o -g
gcc -o build/result build/add_one.o src/main.c -m32 -g

