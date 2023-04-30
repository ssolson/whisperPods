"""
This module provides a function to search for MP3 files in a specified
directory and its subdirectories.

The `find_mp3_files` function takes the root directory as an argument
and returns a list of file paths to all MP3 files found in that 
directory and its subdirectories.
"""
import os
import fnmatch

def find_mp3_files(path):
    """
    Searches for MP3 files in the specified directory and its subdirectories.
    
    Parameters
    ----------
    path : str
        The root directory to search for MP3 files.
    
    Returns
    -------
    list of str
        A list of file paths to all MP3 files found.
    
    Example
    -------
    >>> find_mp3_files("/path/to/music/library")
    ['/path/to/music/library/song1.mp3', '/path/to/music/library/album/song2.mp3']
    """
    mp3_files = []

    for root, _, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, "*.mp3"):
            mp3_files.append(os.path.join(root, filename))

    return mp3_files
