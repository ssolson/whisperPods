import getpodcast

podcasts = {'tdg':  "https://thedailygwei.libsyn.com/rss"}
opt = getpodcast.options(
    date_from= "2023-04-25", 
    list= True,   
    )

getpodcast.getpodcast(podcasts, opt)
