#!/bin/bash

if [ -d "./lib" ]; then
    rm -rf ./lib
    mkdir ./lib
else
    mkdir ./lib
fi

echo "Compilando la librería dinámica en C..."
gcc -shared -W -o ./lib/libaddToGINI.so ./src/add_to_GINI.c 

echo "Compilacion exitosa, librería compilada y guardada en ./lib..."
