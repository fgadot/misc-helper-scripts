# When Microsoft save a CSV file, all variables are coma separated.
# Some softwares will require you to have the values in between double quotes.
# This script does exactly this. It takes two arguments:
# 1) original file
# 2) output file

import csv
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py input_file.csv output_file.csv")
    sys.exit(1)

input_file = sys.argv[1]  # First command line argument
output_file = sys.argv[2]  # Second command line argument

try:
    with open(input_file, newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)  # This ensures all values are quoted

        for row in reader:
            writer.writerow(row)

    print("File processed. Check:", output_file)
except Exception as e:
    print("An error occurred:", e)
