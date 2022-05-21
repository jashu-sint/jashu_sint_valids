import requests
import json

email = ("YOUR_EMAIL")
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

params = {
        'validate': '1',
        'email': email,
    }

r = requests.get( 'https://spclient.wg.spotify.com/signup/public/v1/account',headers=headers,params=params)

if r.json()["status"]==20:

  print(f"{email} ==>Exist In SPOTIFY")

else:
  print(f"{email} ==>Not Exist in SPOTIFY")
