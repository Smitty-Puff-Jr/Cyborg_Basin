import json
import requests
from random import randint

food = input('What are you eating? ')
url = f'https://api.punkapi.com/v2/beers?food={food}'


r = requests.get(url)
data = json.loads(r.text)

beer_list = []

for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']

    beer_item = {
        'name': name,
        'tagline': tagline,
        'abv': abv,
    }
    beer_list.append(beer_item)

value = randint(0, len(beer_list))

try_this = beer_list[value]

print(f'If you are eating {food}, then you should try {try_this['name']}, {try_this['tagline']}, {try_this['abv']}% abv.')
