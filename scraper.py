"""
Using a generator to parse API results
"""

import json
import requests

def crawl():
    response = requests.get('https://swapi.co/api/people/')
    api_results = json.loads(response.content)
    for character in api_results['results']:
        if 'https://swapi.co/api/films/7/' in character['films']:
            yield character['name']

force_awakens = crawl()
for result in force_awakens:
    print(result)