import os
import time

star_time = time.time_ns()

# config (CHANGE THESE)
file_type = '.mp3'
starting_directory = "C:\\directory\\to\\start\\search\\from"  # search this and all nested directories
print_names = False  # change to True to print out the file names + location

def find_files(type, dir, print_or_nah):
    counter = 0
    for root, dirs, files in os.walk(starting_directory):
        for file in files:
            if file.endswith(file_type):
                counter += 1
                if print_or_nah is True:
                    print(os.path.join(root, file))
    return f"{counter} {file_type}'s found."

print(find_files(file_type, starting_directory, print_names))

print(f"Run time: {time.time_ns() - star_time} ns")  # report how long the process took