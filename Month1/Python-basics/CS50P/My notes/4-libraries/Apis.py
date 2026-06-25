import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

# send a GET request to the iTunes Search API
# the search term comes from sys.argv[1] (the word the user typed)
# example URL:
# https://itunes.apple.com/search?entity=song&limit=1&term=beatles
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[1])

# response.json() converts the API response (JSON text) into a Python dictionary
# json.dumps(..., indent=2) converts it back into nicely formatted JSON for printing
# indent=2 just makes it easier to read
print(json.dumps(response.json(),indent=2))


# for each song in the results list,
# print the value associated with the key "trackName"
# this prints the name of the song
o = response.json()
for result in o["results"]:
    print(result["trackName"])