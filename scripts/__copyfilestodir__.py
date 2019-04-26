def CopyFilesToDir(rootdir, dir_to_copy_to, subdirs_to_ignore, dirs_to_loop_through, files_should_contain, test_mode):
    """
    This function copies desired files from one directory to another:
        rootdir: the starting directory path
        dir_to_copy_to: the destination directory
        subdirs_to_ignore: a list of key words to look for in directories you want to ignore
        dirs_to_loop_through: a list of key words to look for in directories you want to loop through
        files_should_contain: a list of key words to look for in files you want to be copied 

        will return a list of the files copied

        enabling test_mode will only print which files would be copied in live mode
    """
    import os
    from shutil import copy2
    files_copied = []

    # looping through the rootdir
    for subdir, dirs, files in os.walk(rootdir):
        # dirs to look in
        if any(_dir in subdir for _dir in dirs_to_loop_through):
            # loop through files
            for file in files:
                # key words to look for in files
                for val in files_should_contain:
                    # logic to select/copy file to destination directory
                    if val in file:
                        # subdirs to ignore
                        if any(_sdir in subdir for _sdir in subdirs_to_ignore):
                            continue
                        if file not in files_copied:
                            if test_mode == False:
                                copy2(os.path.join(subdir, file), dir_to_copy_to)
                            files_copied.append(file)

    return files_copied


print()
user_input = str(input(
    'Press "t" to run in test mode or "c" for files to be copied to the chartrounds folder: ')).lower()
# variables
rootdir = 'C:\\RootFolder'
dir_to_copy_to = 'C:\\DestinationFolder'
subdirs_to_ignore = ['sample1-', '__sample2__']
dirs_to_loop_through = ['_target1', '__target2']
files_should_contain = ['_0', '_1']

# function:
# CopyFilesToDir(rootdir, dir_to_copy_to, subdirs_to_ignore, dirs_to_loop_through, files_should_contain)

if user_input == 't':
    files = CopyFilesToDir(rootdir, rootdir, subdirs_to_ignore,
                           dirs_to_loop_through, files_should_contain, True)
    print()
    print('----- TEST MODE -----')
    print()

elif user_input == 'c':
    files = CopyFilesToDir(rootdir, dir_to_copy_to, subdirs_to_ignore,
                           dirs_to_loop_through, files_should_contain, False)
    print()
    print('----------------------------------------')
    print()

else:
    files = []
    print()
    print('----------------------------------------')
    print()
    input('invalid input, press enter 2x to exit')
    print()
    print('----------------------------------------')
    print()


print('Files Copied: ', len(files))
print('----------------------------------------')
for f in sorted(files):
    print(f)

print()
print('----------------------------------------')
print()

input("Press enter to exit...")
