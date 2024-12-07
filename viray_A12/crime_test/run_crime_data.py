from validate_functions import load_csv, validate_vict_sex, validate_vict_age
from stats_function import load_csv, calculate_mean_age, calculate_median_age 

#load csv
file_path = 'Crime_Data_from_2020_to_Present.csv'  # Change this to the correct path if necessary
data = load_csv(file_path)

#run validation
if validate_vict_sex(data):
    print("All entries in 'Vict sex' are valid.")
else:
    print("Some entries in 'Vict sex' are invalid.")

if validate_vict_age(data):
    print("All entries in 'Vict age' are valid.")
else:
    print("Some entries in 'Vict age' are invalid.")

#run mean and median calculations
mean_age = calculate_mean_age(data)
print(f"Mean Age: {mean_age}")

median_age = calculate_median_age(data)
print(f"Median Age: {median_age}")
