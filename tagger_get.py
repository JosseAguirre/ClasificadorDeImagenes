import pip._vendor.requests as requests
import json

api_key = 'acc_06c14a773d5eab6'
api_secret = 'cc27cca36810dc09120bdd92eef9ea1b'
image_url = 'https://www.havolinedeportivo.com/wp-content/uploads/2022/03/Hinchas-Ecuador.jpeg'
langs = 'en,es'

response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s&language=%s' % (
        image_url, langs),
    auth=(api_key, api_secret)
)
data = response.json()

for tag in data["result"]["tags"]:
    print(tag)

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
