#!/bin/bash

if [ -d "./lib" ]; then
    rm -rf ./lib
    mkdir ./lib
else
    mkdir ./lib
fi

if [ -d "./build" ]; then
    rm -rf ./build
    mkdir ./build
else
    mkdir ./build
fi

echo "Compilando la librería dinámica en C..."
nasm -f elf32 src/add_one.asm -o build/add_one.o
gcc -shared -W -o lib/libaddToGINI.so src/add_to_GINI.c build/add_one.o -m32

echo "Compilacion exitosa, librería compilada y guardada en ./lib..."
