"""
This file is used to clean the csv files.
Using mysqlimport imports the string with the quotes thereby requiring additional quotes in the queries.
Thus we are using this file to clean the strings, essentially removing their quotes
"""
from __future__ import print_function
from sys import argv, exit

def get_proper_line(line):
    line_parts = line.split(",")
    for i in range(len(line_parts)):
        line_parts[i] = line_parts[i].strip()
        if len(line_parts[i]) > 2 and line_parts[i][0] == '"' and line_parts[i][-1] == '"':
            line_parts[i] = line_parts[i][1:-1]
    return ",".join(line_parts)

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: %s <input_path_to_csv_file> <output_path>", argv[0])
        exit(1)

    file_lines = None
    with open(argv[1], "r") as f:
        file_lines = f.readlines()

    with open(argv[2], "w+") as f:
        for line in file_lines:
            line = get_proper_line(line)
            print(line, file=f)
