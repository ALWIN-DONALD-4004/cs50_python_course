# pypi.org/project/requests

#APIs

# itune.py

import sys
import requests
import json 

if len(sys.argv)!=2:
    sys.exit()
 
 #JSON - language agnostic format that changing data with computer   
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent=2))
o = response.json()

for result in o["results"]:
    print(result["trackName"])

