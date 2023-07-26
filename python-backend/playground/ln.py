from listennotes import podcast_api
import pandas as pd
import json


api_key = '503eab868f074b739dcbcce900416e90'
id_the_dily_gwei = '6539d2da4ba54cfb8e00873a5ce85d18'


client = podcast_api.Client(api_key=api_key)
response = client.fetch_podcast_by_id(
  id=id_the_dily_gwei,
  next_episode_pub_date=0,
  sort='recent_first',
)
print(json.dumps(response.json()))

import ipdb; ipdb.set_trace()