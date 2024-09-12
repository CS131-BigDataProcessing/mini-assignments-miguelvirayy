#!/bin/bash

#Activity 1: Displaying Messages
echo "The time and date are: "
date

echo "Let's see who is logged on to the system:"
who

echo "For $USER, the home directory is $HOME"

#Activity 2: Working with positional arguements
name=$1
money=$2
echo "My name is $name and I have \$$money in my wallet"

#Activity 3: Math Time
mathvar1=($[1+5])
mathvar2=($[$mathvar1*20])
mathvar3=10
mathvar4=($[$mathvar1*$[$mathvar2+$mathvar3]])
echo "Variable 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable 3, our final Variable 4 is $mathvar4"

#Activity 4: More math. Working with floating-point solution
floating=$(echo "scale=3; 4.5/1.7" | bc)
echo "Our floating variable is $floating."
