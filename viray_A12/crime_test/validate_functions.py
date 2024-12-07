import csv

def load_csv(file_path): #load csv
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def validate_vict_sex(data): #checks column exists and if entries are only M or F
    for row in data:
        if row['Vict Sex'] not in ['M', 'F']:
            return False
    return True

def validate_vict_age(data): #checks if age is between 1-100
    for row in data:
        try:
            age = int(row['Vict Age'])
            if age < 1 or age > 100:
                return False
        except (ValueError, KeyError):
            return False
    return True

