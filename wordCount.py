# Author: Russell Gehan
# Date: 9-1-2019
# Subject: Theory of Operating Systems
# Assignment: python intro


import sys
import os
import os.path
from os import path

def get_array_from_file(file_name):
    my_file = open(file_name, "r")
    if my_file.mode == 'r':
        # Make sure the program is case-insensitive and ignores special characters.
        file_content = my_file.read()
        file_content = file_content.replace(",", "")
        file_content = file_content.replace("\n", " ")
        file_content = file_content.replace(";", "")
        file_content = file_content.replace(".", "")
        file_content = file_content.replace(":", "")
        file_content = file_content.replace("'", " ")
        file_content = file_content.replace("--", "")
        file_content = file_content.lower()
        array = file_content.split(" ")
        return array
    else:
        return "Could not read file"


def write_results_into_new_file(new_file_name, results):
    if path.exists(new_file_name):
        os.remove(new_file_name)
    new_file = open(new_file_name, "w+")
    for i in range(len(results)):
        new_file.write(results[i][0] + " " + str(results[i][1]) + "\n")


def generate_list_of_unique_words(array):
    new_dict = []
    for i in range(len(array)):
        if len(new_dict) < 1:
            new_dict.append([array[i], 1])
            continue
        if array[i] == "":
            continue
        pos = binary_search(new_dict, array[i], 0, len(new_dict) - 1)
        # print("Resulting position " + str(pos))
        if array[i] == new_dict[pos][0]:
            new_dict[pos][1] += 1
        else:
            if array[i] < new_dict[pos][0]:
                new_dict.insert(pos, [array[i], 1])
            else:
                new_dict.insert(pos+1, [array[i], 1])
        # print("My list so far: " + str(new_dict))
    return new_dict


def binary_search(my_list, item, low, high):
    if high > low:
        mid = int((low + high) / 2)
        # print(str(low) + " " + str(mid) + " " + str(high) + " " + str(len(my_list)))
        if my_list[mid][0] == item:
            return mid
        if my_list[mid][0] > item:
            return binary_search(my_list, item, low, mid - 1)
        else:
            return binary_search(my_list, item, mid + 1, high)
    else:
        return int((low + high) / 2)


arg = sys.argv
if len(arg) > 1:
    if path.exists(arg[1]):
        arr_from_file = get_array_from_file(arg[1])
        results = generate_list_of_unique_words(arr_from_file)
        for i in range(len(results)):
            print(results[i][0] + " " + str(results[i][1]))
        if len(arg) > 2:
            write_results_into_new_file(arg[2], results)
        else:
            print("No output file specified.")
    else:
        print("Input file not found.")
else:
    print("You didn't give me a file.")
