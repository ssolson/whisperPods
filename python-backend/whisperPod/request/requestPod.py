import getpodcast

def get_podcast(url, name, start_at, path="./podcast"):
    """
    Download a podcast from a given url and save it to a given path.
    
    PARAMETERS
    ----------
    url : str
        The url of the podcast to download.
    name : str
        The name of the podcast to download.
    start_at : str  
        The date from which to download the podcast.
    path : str
        The path to save the podcast to.

    RETURNS
    -------
    None
    """
    podcasts = {name:  url}
    opt = getpodcast.options(
        date_from=start_at,
        root_dir=path,
        template="{rootdir}/{podcast}/{title}{ext}"
        )

    getpodcast.getpodcast(podcasts, opt)
