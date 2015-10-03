# coding: utf-8
from Chap03_025 import extract_country_data
import urllib.request, urllib.parse
import json

dic_country_data = extract_country_data()

endpoint = "https://en.wikipedia.org/w/api.php?"
params = urllib.parse.urlencode({
    "action": "query", 
    "prop": "imageinfo", 
    "format": "json", 
    "iiprop": "url", 
    "titles": "File:"+dic_country_data['国旗画像']
})

page_url = endpoint + params
with urllib.request.urlopen(page_url) as page:
    dic_page = json.loads(page.read().decode('utf-8'))
    page_id = str(list(dic_page['query']['pages'].keys())[0])
    print(dic_page['query']['pages'][page_id]['imageinfo'][0]['url'])