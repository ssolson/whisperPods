import getpodcast

opt = getpodcast.options(
    date_from='2023-04-20',
    root_dir='./podcast')

podcasts = {
    "thedailygwei": "https://thedailygwei.libsyn.com/rss"    
}

getpodcast.getpodcast(podcasts, opt)
