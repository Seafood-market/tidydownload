import os
import time

def search_old_file_(folder_path :str, days :int = 30):
    """
    Find all files in the specified folder that have not
    been modified for more than the specified number of days.

    parameter:
        folder_path: The path to the folder to search
        days: The number of days since the file was last modified

    return:
        a list containing paths to all old files
    """

    old_files = []
    current_time = time.time()

    for filename in os.listdir(folder_path):
        # Get the full location of the file
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        if os.path.getatime(file_path) < current_time - days * 86400:
            old_files.append(file_path)

    return old_files

def delete_files(file_list: list):
    """
    Delete all files in the given list

    parameter:
        file_list: a list of paths to the files to be deleted
    """

    for file_path in file_list:
        os.remove(file_path)

def cleanup_old_files(folder_path, days = 30):
    """
    Clean up all files in the specified folder that have not 
    been modified for a specified number of days.

    parameter:
        folder_path: the path of the folder to be cleaned up
        days: The number of days since the file was last modified
    """

    old_files = search_old_file_(folder_path, days)

    delete_files(old_files)
