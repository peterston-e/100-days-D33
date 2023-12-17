import json

import requests
import pandas

response = requests.get("https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json#")
response.raise_for_status()
data = response.json()
df = pandas.DataFrame(data["soles"])
print(df)


# with open("data.json", "w") as file:
#     json.dump(data["soles"], file, indent=4)
#     df = pandas.read_json("data.json")
#     print(df)
