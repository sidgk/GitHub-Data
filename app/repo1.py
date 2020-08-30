import json
from urllib.request import urlopen

with urlopen("https://api.github.com/repos/sidgk/DeliveryHero/commits/8b4393049c3f84800709d35be25f9b30d01bf889") as response:
    source = response.read()

data = json.loads(source)
#print(data)

print(json.dumps(data["files"][0]["filename"], indent=2))
'''for item in data["files"]:
    print(item["filename"])'''

