import requests
import json
import os
import time

def scrape(base_url, output_file):
    """
    Scrape metadata of all episodes from a given podcast base URL and 
    save it to a given output file.
    
    PARAMETERS
    ----------
    base_url : str
        The base URL of the podcast to scrape metadata from.
    output_file : str
        The name of the output file to save the scraped metadata.

    RETURNS
    -------
    all_episodes : list
        A list of dictionaries containing metadata of all episodes.
    """
    # Load last checkpoint if it exists
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            all_episodes = json.load(f)
            last_page = all_episodes[-1]['page']
    else:
        all_episodes = []
        last_page = 0

    page = last_page + 1

    while True:
        request_url = f"{base_url}/page/{page}/render-type/json"
        response = requests.get(request_url)
        episodes = json.loads(response.text)

        # Break the loop if there are no more episodes
        if not episodes:
            break

        # Add the page number to each episode
        for episode in episodes:
            episode['page'] = page

        all_episodes.extend(episodes)

        # Save the results every 10 requests
        if page % 10 == 0:
            with open(output_file, 'w') as f:
                json.dump(all_episodes, f)

        page += 1

        # Wait for 1-2 seconds before making another request
        print((all_episodes[-1]['release_date']))
        time.sleep(1.5)

    # Save the final results
    with open(output_file, 'w') as f:
        json.dump(all_episodes, f)

    return all_episodes
