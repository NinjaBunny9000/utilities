import os
import time

star_time = time.time_ns()

# config (CHANGE THESE)
find_dir = "C:\\directory\\to\\find\\files\\in"  # search this and all nested directories
print_names = True  # change to True to print out the file names + location


def find_and_move(find_dir, print_or_nah):
    counter = 0
    for root, dirs, files in os.walk(find_dir):
        for file in files:
            counter += 1
            if print_or_nah is True:
                # print(os.path.join(root, file))
                print(f"{file}")
    return f"\n{counter} files located."


print(find_and_move(find_dir, print_names))

print(f"Run time: {time.time_ns() - star_time} ns")  # report how long the process took