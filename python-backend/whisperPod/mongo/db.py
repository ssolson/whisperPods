import os
import re
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_client():
    # Construct the environment file path relative to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_file_path = os.path.join(script_dir, '../../../mongo/config.env')

    # Get the URI from the environment file
    with open(env_file_path, 'r') as file:
        content = file.read()

    pattern = r"ATLAS_URI=(.*)"
    result = re.search(pattern, content)

    if result:
        uri = result.group(1)

        # Set the Stable API version when creating a new client
        client = MongoClient(uri, server_api=ServerApi('1'))
                                
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        return client

    else:
        print("No match found")
        return Warning("No match found")