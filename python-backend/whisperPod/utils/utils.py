"""
This module provides a function to search for MP3 files in a specified
directory and its subdirectories.

The `find_mp3_files` function takes the root directory as an argument
and returns a list of file paths to all MP3 files found in that 
directory and its subdirectories.
"""
import os
import fnmatch


def find_mp3_files(path, recursive=True):
    """
    Searches for MP3 files in the specified directory and its subdirectories.

    Parameters
    ----------
    path : str
        The root directory to search for MP3 files.
    recursive : bool
        Whether to search subdirectories of the root directory.

    recursive : bool, default=True
        Whether to search recursively in subdirectories.

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

    if recursive:
        for root, _, filenames in os.walk(path):
            for filename in fnmatch.filter(filenames, "*.mp3"):
                mp3_files.append(os.path.join(root, filename))
    else:
        for filename in os.listdir(path):
            if filename.endswith(".mp3"):
                mp3_files.append(os.path.join(path, filename))

    return mp3_files


def combine_metadata(podcast_metadata, yt_metadata):
    combined_metadata = []
    unmatched_metadata = []

    for podcast_item in podcast_metadata:
        matched = False
        for yt_item in yt_metadata:
            if podcast_item["item_title"] == yt_item["title"]:
                combined_item = podcast_item.copy()

                for key, value in yt_item.items():
                    combined_item["yt_" + key] = value

                combined_metadata.append(combined_item)
                matched = True
                break

        if not matched:
            unmatched_metadata.append(podcast_item)

    return combined_metadata, unmatched_metadata
