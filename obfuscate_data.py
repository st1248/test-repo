import csv
import random
import string

# Sample replacement names
FIRST_NAMES = ["Alex", "Jamie", "Taylor", "Jordan", "Morgan", "Casey", "Riley", "Drew"]
LAST_NAMES = ["Smith", "Johnson", "Lee", "Brown", "Jones", "Garcia", "Miller", "Davis"]

def random_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def mask_ssn(ssn):
    # Mask all but last 4 digits
    parts = ssn.split('-')
    if len(parts) == 3:
        return f"XXX-XX-{parts[2]}"
    return "XXX-XX-XXXX"

def mask_cc(cc):
    # Mask all but last 4 digits
    cc = cc.replace('-', '')
    if len(cc) == 16:
        return f"XXXX-XXXX-XXXX-{cc[-4:]}"
    return "XXXX-XXXX-XXXX-XXXX"

def obfuscate_row(row):
    row[0] = random_name()
    row[1] = mask_ssn(row[1])
    row[2] = mask_cc(row[2])
    return row

def obfuscate_file(input_file, output_file):
    with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')
        header = next(reader)
        writer.writerow(header)
        for row in reader:
            writer.writerow(obfuscate_row(row))

if __name__ == "__main__":
    print("Usage: python obfuscate_data.py <input_file> <output_file>")
    print("Input file should be tab-delimited with columns: First and Last Name, SSN, Credit Card Number")
