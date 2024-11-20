#!/bin/bash

#Remove trailing spaces and lines
echo "Removing trailing spaces and lines..."

sed -i 's/[ \t]*$//' AB_NYC_2019.csv

#Replace missing fields with N/A
echo "Replacing missing fields with N/A..."

awk -F, ' BEGIN { OFS = "," } 
{
  for (i = 1; i <= 16; i++) {
    if ($i ~ /^ *$/) {
      $i="N/A";
    }
  }
  print $0
}' AB_NYC_2019.csv > AB_NYC_2019_clean.csv

#Remove Duiplicate Entries
echo "Removing duplicate Entries..."

sort -t ',' -k1 AB_NYC_2019_clean.csv | uniq > AB_NYC_2019_unique.csv


#Identify outliers using mode and delete 

echo "Removing outliers..."

awk -F',' -v OFS=',' 'BEGIN { FPAT = "([^,]+)|(\"[^\"]+\")" } { print $10 }' AB_NYC_2019_unique.csv > temp.txt

mean=$(awk '{ total += $1; count++ } END { print total / count }' temp.txt)

rounded_mean=150

#find IQR for outliers
sorted_data=$(sort -n temp.txt)

num_rows=$(wc -l < temp.txt)

q1_index=$(( (num_rows + 1) / 4 ))
q3_index=$(( 3 * (num_rows + 1) / 4 ))


q1=$(echo "$sorted_data" | sed -n "${q1_index}p")
q3=$(echo "$sorted_data" | sed -n "${q3_index}p")

iqr=$(echo "$q3 - $q1" | bc)


echo "$iqr"

upper=160

echo "$lower"

awk -F ',' -v OFS=',' 'BEGIN { FPAT = "([^,]+)|(\"[^\"]+\")" } $10 <= $upper && $10 > 0 { print $0 }' AB_NYC_2019_unique.csv > AB_NYC_2019_final.csv




