#!/bin/bash

#Remove trailing spaces and lines
echo "remove trailing spaces and lines..."

sed -i 's/[[:space:]]\+$//' "house_sales.csv"

#Remove rows with missing values
echo "Removing rows with missing values..."

awk '{for(i=1;i<=22;i++) if($i=="0") $i="N/A"; print}' house_sales.csv > cleaned_house_sales.csv

#Remove Duiplicate Entries
echo "Removing duplicate Entries..."

sort -t’\t’ -k1 cleaned_house_sales.csv | uniq > output.csv

sort -t' ' cleaned_house_sales.csv | uniq > unique_house.csv


#Identify outliers and replace with mode
awk -F’\t’ '$3 > 10000000 { print NR, $0 }' cleaned_house_sales.csv

cut -d$'\t' -f3 cleaned_house_sales.csv > field_values.txt

mode_value=$(sort field_values.txt | uniq -c | sort -nr | head -n 1 | awk '{print $3}')

awk -F'\t' -v mode="$mode_value" '{ if ($3 == "") $3 = mode; print $0 }' OFS='\t' cleaned_house_sales.csv > house_imputed.csv

