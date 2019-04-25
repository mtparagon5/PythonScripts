import os
from shutil import copy2

rootdir = '..//'
midtown = '_midtown'
clifton = '_clifton'
chartrounds_dir = 'S:\\shares\\RadOnc\\ePHI\\RO PHI CONF IMAGES\\_Chart Rounds PDFs'
printouts_dir = 'H:\\printouts'

def CopyFilesToDir(rootdir, dir_to_copy_to, subdirs_to_ignore, dirs_to_loop_through, files_should_contain):
    # """
    # This function will loop through each subdir in rootdir and 
    # each file in subdir, if file contains _0 or _1 it means it 
    # contains a date, which means it is a tx planning report for 
    # a patient this will then copy each file matching that 
    # description into the chartrounds folder.
    # """
    """
    This function copies desired files from one directory to another:
        rootdir: the starting directory path
        dir_to_copy_to: the destination directory
        subdirs_to_ignore: a list of key words to look for in directories you want to ignore
        dirs_to_loop_through: a list of key words to look for in directories you want to loop through
        files_should_contain: a list of key words to look for in files you want to be copied 
        
        will return a list of the files copied
    """
    files_copied = []
    # looping through the rootdir
    for subdir, dirs, files in os.walk(rootdir):
        # subdirs to ignore
        for _sdir in subdirs_to_ignore:
            # dirs to look in
            for _dir in dirs_to_loop_through:
                # logic
                if _dir in subdir and _sdir not in subdir:
                    # loop through files
                    for file in files:
                        # key words to look for in files
                        for val in files_should_contain:
                            # logic to select/copy file to destination directory
                            if val in file:
                                copy2(os.path.join(subdir, file), dir_to_copy_to)

                                files_copied.append(file)
    return files_copied

subdirs_to_ignore = ['z-']
dirs_to_loop_through = ['_midtown', '_clifton']
files_should_contain = ['_0', '_1']

print(CopyFilesToDir(rootdir, rootdir, subdirs_to_ignore, dirs_to_loop_through, files_should_contain))