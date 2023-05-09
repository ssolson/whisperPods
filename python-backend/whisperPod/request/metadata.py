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
            # import ipdb
            # ipdb.set_trace()
            existing_episode_ids = {
                episode['item_id']for episode in all_episodes
            }
    else:
        all_episodes = []
        existing_episode_ids = set()

    page = 1
    new_episodes = True

    while new_episodes:
        new_episodes = False
        request_url = f"{base_url}/page/{page}/render-type/json"
        response = requests.get(request_url)
        episodes = json.loads(response.text)

        # Break the loop if there are no more episodes
        if not episodes:
            break

        for episode in episodes:
            # Check if the episode is not in the existing set
            if episode['item_id'] not in existing_episode_ids:
                new_episodes = True
                existing_episode_ids.add(episode['item_id'])
                all_episodes.append(episode)

                # Save the results every 10 requests
                if len(all_episodes) % 10 == 0:
                    with open(output_file, 'w') as f:
                        json.dump(all_episodes, f)

                # Wait for 1-2 seconds before making another request
                print(episode['release_date'])
                time.sleep(1.5)

        page += 1

    # Save the final results
    with open(output_file, 'w') as f:
        json.dump(all_episodes, f)

    return all_episodes
