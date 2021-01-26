import requests
#import secrets

base_uri = "https://api.myanimelist.net/v0"
endpoints = {
    'auth' : 'https://myanimelist.net/v1/oauth2/authorize',
    'get_anime_list': base_uri + '/anime',
    'get_anime_details': base_uri + '/anime'
}
#credentials = {}

#Sets client id and secret
# Not needed for this project
# def read_credentials():
        
#     f = open(text_file,'r')

#     #get token line
#     token = f.readline()
#     token = token.split('mal_id:')[1]
#     credentials['client_id'] = token

#     token = f.readline()
#     token = token.split('mal_secret:')[1]
#     credentials['client_secret'] = token

# def get_new_code_verifier():
#     token = secrets.token_urlsafe(100)
#     return token[:128]

# Search for an anime
# Q - search, limit - default is 100 with a max of 100, offset - default is 0, fields - string
def get_anime_list(q,fields,limit=100,offset=0,):
    print(endpoints['get_anime_list'])
    r = requests.get(endpoints['get_anime_list'],
        params=
        {
            'q':q,
            'limit':limit,
            'offset':offset,
            'fields':fields
        })
    return r
def get_anime_details(id,fields=''):
    r = requests.get(endpoints['get_anime_details']+'/' +str(id),params = {'fields':fields})
    return r
if __name__ == '__main__':
    # r = get_anime_list('one','',limit = 1)
    # print(r)
    # print(r.text)
    
    # code_verifier = code_challenge = get_new_code_verifier()

    # print(len(code_verifier))
    # print(code_verifier)
    r = get_anime_details(22,'id,alternative_titles')
    print(r.text)