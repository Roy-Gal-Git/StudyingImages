import sys
import os
from PIL import Image


def print_enumerated_list(lst):
    counter = 0
    for item in lst:
        print(str(item[0]) + ". \"" + str(item[1] + "\""))
        counter += 1


def set_dir():
    # C:\Users\Roy.DEV\Desktop\Python\Studying Images
    cwd = os.getcwd()
    print(f"the current working directory is {cwd}.",
          "\nWould you like to change the current working directory?")
    while True:
        pick = input("Y/N: ")
        pick = pick.upper()

        if pick == "Y":
            path = input("Enter a path:")
            os.chdir(path)
            cwd = os.getcwd()
            break
        elif pick == "N":
            break
        else:
            continue

    dir_list = []
    for directory in os.listdir(cwd):
        if os.path.isdir(directory):
            dir_list.append(directory)
        else:
            continue

    for i, d in enumerate(dir_list):
        dir_list[i] = [i, d]

    print_enumerated_list(dir_list)


set_dir()


# cwd = os.getcwd()
# next_dir = "\\Pokedex"
# check_dir = "\\new"

# while True:
#     if os.path.exists(cwd + next_dir + check_dir):
#         for img in os.listdir(cwd + next_dir):
#             print(img)
#         break
#     else:
#         os.mkdir(cwd + next_dir + check_dir)
