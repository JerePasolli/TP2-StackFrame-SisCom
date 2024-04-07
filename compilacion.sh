#!/bin/bash

if [ -d "./include" ]; then
    rm -rf ./include/*
else
    mkdir ./include
fi

echo "Compilando la librería dinámica en C..."
gcc -shared -W -o libaddToGINI.so add_to_GINI.c 

echo "Compilacion exitosa, librería compilada y guardada en ./include..."
