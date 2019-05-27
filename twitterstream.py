import requests
from requests_oauthlib import OAuth1
import jsonlines

api_key = "NABkOiCt1RCrHb9VUPQ6T4obk"
api_secret = "Ez8eXJDMC26hKSxtdwATk24arQrsb6OO9ITXg9MptKRLgaVjUC"
access_token_key = "1129107025852547073-99ZPjAtBdE1Wk344pxBz3DEaQwnxfr"
access_token_secret = "SoRZXueMcACGOHZwXd50M9HwybrPCzWM72bA6Drg2Q6rD"

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth)
print(r.status_code)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'

with jsonlines.open('output.json', mode='w') as writer:    
    try:
        for line in r.iter_lines(decode_unicode=True):
            if line:
                writer.write(line)
    except KeyboardInterrupt:
        pass
