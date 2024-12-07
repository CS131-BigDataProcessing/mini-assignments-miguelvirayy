import csv

def load_csv(file_path): #load ata
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        return data

def calculate_mean_age(data): #calculate mean age
    ages = [int(row['Vict Age']) for row in data if row['Vict Age'].isdigit()]
    if not ages:
        raise ValueError("No valid ages found in the data.")
    return sum(ages) / len(ages)

def calculate_median_age(data): #calculate median age
    ages = sorted(int(row['Vict Age']) for row in data if row['Vict Age'].isdigit())
    if not ages:
        raise ValueError("No valid ages found in the data.")
    mid = len(ages) // 2
    return (ages[mid] if len(ages) % 2 != 0 else (ages[mid - 1] + ages[mid]) / 2)

