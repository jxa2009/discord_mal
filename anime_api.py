import requests

base_uri = "https://api.myanimelist.net/v0"

# Search for an anime
# Q - search, limit - default is 100 with a max of 100, offset - default is 0, fields - string
def search_anime(q,fields,limit=100,offset=0,):
    return requests.get(base_uri,params={'q':q,'limit':limit,'offset':offset,'fields':fields})

print(search_anime('one',''))