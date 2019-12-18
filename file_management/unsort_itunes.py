import os
import shutil
import time

star_time = time.time_ns()

# config (CHANGE THESE)
file_types = ['mp3', 'wav', 'ogg', 'aif', 'aiff', 'm4a', 'm4p', 'm4b']
ignored = ['Thumbs.db', '.DS_Store']
find_dir = "C:\\directory\\to\\move\\music\\from"  # search this and all nested directories
move_dir = "C:\\directory\\to\\move\\music\\to"  # move files found to this director
unnest_dir = "C:\\directory\\to\\move\\put\\everything\\else"  # move the rest of the unnested files here
print_names = False  # change to True to print out the file names + location

def find_and_move(file_types, find_dir, move_dir, unnest_dir, print_or_nah):
    music = 0
    non_music = 0

    # walk through all the directories
    for root, dirs, files in os.walk(find_dir):
        for file in files:

            # try and grab the file type
            try:
                file_type = file.split('.')[-1].strip().lower()
            except IndexError:
                pass

            # move music to move_dir
            if file_type in file_types:
                music += 1
                shutil.move(f"{root}\\{file}",f"{move_dir}\\{file}")
                if print_or_nah is True:
                    print(f"{file[-4:]} moved.")

            # move everything else except ignored files to the unnest_dir
            elif file not in ignored:
                try:
                    shutil.move(f"{root}\\{file}",f"{unnest_dir}\\{file}")
                    non_music += 1
                except FileExistsError:
                    print(f"FileExistsError: {file}")
                except PermissionError:
                    print(f"PermissionError: {file}")
                if print_or_nah is True:
                    print(f"{file} moved.")

    print(f"\n{music} music files moved to {move_dir}")
    print(f"{non_music} other files moved to {unnest_dir}.")


find_and_move(file_types, find_dir, move_dir, unnest_dir, print_names)  # run the find and move operation
print(f"\nRun time: {time.time_ns() - star_time} ns")  # report how long the process took