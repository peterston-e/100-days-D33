import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

lat = data['iss_position']['latitude']
long = data['iss_position']['longitude']
iss_position = (lat, long)
print(iss_position)
print(f"{lat}, {long}")
