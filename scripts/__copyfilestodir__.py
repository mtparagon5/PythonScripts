def CopyFilesToDir(rootdir, dir_to_copy_to, subdirs_to_ignore, dirs_to_loop_through, files_should_contain):
    """
    This function copies desired files from one directory to another:
        rootdir: the starting directory path
        dir_to_copy_to: the destination directory
        subdirs_to_ignore: a list of key words to look for in directories you want to ignore
        dirs_to_loop_through: a list of key words to look for in directories you want to loop through
        files_should_contain: a list of key words to look for in files you want to be copied 

        will return a list of the files copied
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
                        copy2(os.path.join(subdir, file), dir_to_copy_to)
                        files_copied.append(file)

    return files_copied
