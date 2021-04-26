#! /usr/bin/bash
echo "Hello world!"
NAME="Jose"
echo "Mi nombre es $NAME"
read -p "Enter your name:" NAME2
echo "Mi otro nombre es $NAME2"
if [$NAME == $NAME2] then
    echo "Son el mismo nombre" else
    echo "NO son el mismo nombre" fi