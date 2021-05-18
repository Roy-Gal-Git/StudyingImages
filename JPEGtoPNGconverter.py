import os
from PIL import Image
from termcolor import cprint


def print_enumerated_list(lst):
    counter = 0
    cprint("Directories:", "cyan")
    for item in lst:
        print(str(item[0]) + ". \"" + str(item[1] + "\""))
        counter += 1
    print()


def create_enum_directories(cwd):
    dir_list = []
    for directory in os.listdir(cwd):
        if os.path.isdir(directory):
            dir_list.append(directory)
        else:
            continue

    for i, d in enumerate(dir_list):
        dir_list[i] = [i, d]

    return dir_list


def set_dir():
    # C:\Users\Roy.DEV\Desktop\Python\Studying Images
    cwd = os.getcwd()
    print(f"the current working directory is {cwd}.",
          "\nWould you like to change the current working directory?")
    while True:
        pick = input("Y/N: ")
        pick = pick.upper()

        if pick == "Y":
            path = input("Enter a path: ")
            os.chdir(path)
            cwd = os.getcwd()
            return cwd
        elif pick == "N":
            return cwd
        else:
            continue


def print_jpgs(cwd):
    cprint("JPGs:", "cyan")
    counter = 0
    jpg_list = os.listdir(cwd)
    for item in jpg_list:
        if item.endswith(".jpg"):
            print(str(counter) + ". " + item)
            counter += 1

    if counter > 0:
        cprint("\nWould you like to convert all of the JPGs to PNGs and put them in the \"new\" directory?", "magenta")
        while True:
            pick = str(input("Y/N: "))
            pick = pick.upper()
            if pick == "Y":
                if os.path.exists(cwd + "\\new"):
                    try:
                        new_dir_path = cwd + "\\new"
                        for img in jpg_list:
                            img_pick = Image.open(cwd + "\\" + img)
                            img_pick.save(new_dir_path + "\\" + img[:-4] + ".png")
                    except PermissionError as e:
                        cprint("No permission! Stopping process.", "red")
                    break
                else:
                    while True:
                        try:
                            new_dir_path = cwd + "\\new"
                            os.mkdir(new_dir_path)
                            for img in jpg_list:
                                img_pick = Image.open(cwd + "\\" + img)
                                img_pick.convert('RGB')
                                img_pick.close()
                                img_pick = Image.open(cwd + "\\" + img)
                                img_pick.save(new_dir_path + "\\" + img[:-4] + ".png")
                            break
                        except PermissionError as e:
                            cprint("No permission! Stopping process.", "red")
                            continue
                        break
            elif pick == "N":
                break
            else:
                continue
    else:
        cprint("NO JPGs FOUND\n", "yellow")


def choose_next_dir(cwd, dir_list):
    try:
        print_enumerated_list(dir_list)
        print_jpgs(cwd)
        pick = int(input("Enter the next directory's number: "))
        dir_num = len(dir_list)
        if pick >= dir_num or pick < 0:
            cprint("NOT IN RANGE\n", "red")
            choose_next_dir(cwd, dir_list)
        else:
            for num in dir_list:
                if num[0] == pick:
                    next_dir = "\\" + str(num[1])
                    cwd = cwd + next_dir
                    dir_list = create_enum_directories(cwd)
                    break

            if not dir_list:
                print_jpgs(cwd)

            else:
                choose_next_dir(cwd, dir_list)



    except ValueError as e:
        print("Not a number.")


def main():
    cwd = set_dir()
    if os.path.exists(cwd + "\\new"):
        dir_list = create_enum_directories(cwd)
        choose_next_dir(cwd, dir_list)

    else:
        print("Would you like to create a file named \"new\"?")
        while True:
            pick = str(input("Y/N: "))
            pick = pick.upper()
            if pick == "Y":
                os.mkdir(cwd + "\\new")
                break
            elif pick == "N":
                break
            else:
                continue
        dir_list = create_enum_directories(cwd)
        choose_next_dir(cwd, dir_list)


if __name__ == '__main__':
    main()
