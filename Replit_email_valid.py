import requests
import json

def replit(email):
  data = '{"email":"' + str(email) + '"}'
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'content-type': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'Origin': 'https://replit.com',
        'Connection': 'keep-alive',
    }
  r = requests.post("https://replit.com/data/user/exists", headers=headers, data=data)
  if r.json()['exists']:
    print("True")
  else:
    print("False")

replit("YOUR_EMAIL")
