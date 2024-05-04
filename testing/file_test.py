import csv

f_path = str(
    input("Enter the path to a .txt or .csv file containing hashes :: "))

file = open(f_path, 'r')
print(file.read())
file.close()
