#!/bin/bash

#Actiivty 2: Temperature in California

temperature=$1

if [[ temperature -gt 55 ]]
then 
 if [[ temperature -lt 67 ]]
 then
  echo "cold"
 elif [[ temperature -lt 85 ]]
 then
  echo "nice"
 elif [[ temperature -gt 85 ]]
 then
  echo "hot"
 fi
else
 echo "freezing"
fi
