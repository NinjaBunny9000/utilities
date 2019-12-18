from mutagen.easyid3 import EasyID3
import mutagen
# from mutagen.id3 import ID3
# from mutagen.mp3 import MP3
import mutagen.easyid3
import os
# import shutil
import time
import pprint

star_time = time.time_ns()
pp = pprint.PrettyPrinter()


# config (CHANGE THESE)
file_types = ['mp3', 'wav', 'ogg', 'aif', 'aiff', 'm4a', 'm4p', 'm4b']
ignored = ['Thumbs.db', '.DS_Store']
# find_dir = "Y:\\test"  # search this and all nested directories
find_dir = "C:\\directory\\to\\move\\music\\from"  # search this and all nested directories
move_dir = "C:\\directory\\to\\move\\music\\to"  # move files found to this director
unnest_dir = "C:\\directory\\to\\move\\put\\everything\\else"  # move the rest of the unnested files here
print_names = False  # change to True to print out the file names + location

def id3_renamer(file_types, find_dir, print_or_nah):

    loaded = 0
    failed = 0
    error = 0
    artist_and_title = []
    artist_missing = []
    title_missing = []
    no_tags = []

    # print(EasyID3.valid_keys.keys())

    # walk through all the directories
    for root, dirs, files in os.walk(find_dir):
        for file in files:

            full_path = f"{root}\{file}"
            artist = 'None'
            title = 'None'

            # try and grab the file type
            try:
                file_type = file.split('.')[-1].strip().lower()
            except IndexError:
                pass

            # print_info(full_path)  # DEBUG print out what metadata there is so far


            try:
                track = mutagen.easyid3.EasyID3(full_path)
            except BaseException as e:
                print(f"Loading failed: {e}")
                failed += 1
                continue

            try:
                # check to see if the artist and title tags are empty or nah
                # if track[u'artist'] and track[u'title']:
                if 'artist' in track:
                    artist = track[u'artist'][0]
                if 'title' in track:
                    title = track[u'title'][0]



                # else:
                #     print(f"Missing tags: {file=} {track.keys()=}")
                loaded += 1
                print(f"Track located: {artist} - {title} {track.keys()=}")
            except KeyError as e:
                error += 1
                print(f"Error: {file} {e}")

            if u'artist' in track.keys() and 'title' in track.keys():
                artist_and_title.append(file)

            elif u'artist' not in track.keys() and 'title' in track.keys():
                artist_missing.append(file)

            elif u'artist' in track.keys() and 'title' not in track.keys():
                title_missing.append(file)

            elif u'artist' not in track.keys() and 'title' not in track.keys():
                no_tags.append(file)


    print('\nARTIST AND TITLE')
    pp.pprint(artist_and_title)
    print('\nNO TITLE')
    pp.pprint(title_missing)
    print('\nNO ARTIST')
    pp.pprint(artist_missing)
    print('\nNO TAGS')
    pp.pprint(no_tags)
    print(f"\n{loaded=} {failed=} {error=}")
    print(f"\n{len(artist_and_title)=} {len(title_missing)=} {len(artist_missing)=} {len(no_tags)=}")


            # if the artist and title meta data are available, rename the file <artist> - <title>

            # for frame in f.tags.getall("TXXX"):
            #     print(f"{frame=}")

            # try and grab the file type
            # try:
            #     file_type = file.split('.')[-1].strip().lower()
            # except IndexError:
            #     pass

            # move music to move_dir
            # if file_type in file_types:
            #     pass




def print_info(file_location):
    try:
        # f = mutagen.File(f"{root}\{file}", ID3=EasyID3)
        f = mutagen.easyid3.EasyID3(file_location)
    except BaseException as e:
        print(f"Loading failed: {e}")
        return

    print(f"{f.keys()=}")
    print(f"{f['album'][0]=}")
    print(f"{f['copyright'][0]=}")
    print(f"{f['title'][0]=}")
    print(f"{f['title'][0]=}")
    print(f"{f['language'][0]=}")
    print(f"{f['date'][0]=}")
    print(f"{f['albumartist'][0]=}")

    # f['albumartist'] = u'testing album artist'
    # f.save()


    # f.pprint()
    # print(f"{type(f.tags)=}")
    # print(f"{type(f.info)=}")
    # print(f"{f.pprint()=}")
    # print(f"{f.info.bitrate=}")
    # print(f"{f.tags["title"]}")
    # print(f"{f.keys()=}")  # this can get cray...


    # print(f"\n{music} music files moved to {move_dir}")
    # print(f"{non_music} other files moved to {unnest_dir}.")


id3_renamer(file_types, find_dir, print_names)  # run the find and move operation
print(f"\nRun time: {time.time_ns() - star_time} ns")  # report how long the process took
