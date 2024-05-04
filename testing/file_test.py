import csv

# f_path = str(
#     input("Enter the path to a .txt or .csv file containing hashes :: "))

test_f_path = "C:\\Users\\skydr\\Documents\\Development\\vt_tool\\testing\\test.txt"
f_path = test_f_path


file = open(f_path, 'r')
print(file.read())
file.close()
