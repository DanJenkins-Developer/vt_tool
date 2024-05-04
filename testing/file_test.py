import csv

# f_path = str(
#     input("Enter the path to a .txt or .csv file containing hashes :: "))


def get_hash_list():

    test_f_path = "C:\\Users\\skydr\\Documents\\Development\\vt_tool\\testing\\test.txt"
    f_path = test_f_path

    with open(f_path, "r") as hash_file:
        lines_list = hash_file.read().splitlines()

        # print(lines_list)
    return lines_list
