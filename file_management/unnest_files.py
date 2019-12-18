import os
import shutil
import time

star_time = time.time_ns()

# config (CHANGE THESE)
find_dir = "Y:\\Old iTunes Libraries\\HOLY CRAP OLD ITUNES ACK"  # search this and all nested directories
move_dir = "Y:\\Old iTunes Libraries\\unsorted"  # move files found to this director
print_names = False  # change to True to print out the file names + location


def find_and_move(find_dir, move_dir, print_or_nah):
    counter = 0
    for root, dirs, files in os.walk(find_dir):
        for file in files:
            if file.title() != '.DS_Store':
                counter += 1
                # print(f"{root}\\{file}")
                try:
                    shutil.move(f"{root}\\{file}",f"{move_dir}\\{file}")
                except FileExistsError as e:
                    print(f"{file} not moved: {e}")
                except PermissionError as e:
                    print(f"{file} not moved: {e}")
                if print_or_nah is True:
                    print(f"{file} moved.")
    return f"\n{counter} files moved."


print(find_and_move(find_dir, move_dir, print_names))

print(f"Run time: {time.time_ns() - star_time} ns")  # report how long the process took