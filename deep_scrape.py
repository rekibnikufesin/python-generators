"""
Using a generator to parse API results
and subsequent pages
"""

import json
import requests

def deep_scrape(link):
    "Generator to crawl API pagination"
    response = requests.get(link)
    api_results = json.loads(response.content)
    for character in api_results['results']:
        if 'https://swapi.co/api/films/7/' in character['films']:
            yield character['name']
    if 'next' in api_results and api_results['next'] is not None:
        next_page = deep_scrape(api_results['next'])
        for page in next_page:
            yield page


response = deep_scrape('https://swapi.co/api/people/')
for result in response:
    print(result)