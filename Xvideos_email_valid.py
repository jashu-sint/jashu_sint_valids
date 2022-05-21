import requests
import json

email = "YOUR_EMAIL"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
       'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://www.xvideos.com/',

    }

params = {
        'email': email,
    }

r = requests.get( 'https://www.xv-videos1.com/account/checkemail',headers=headers,params=params)

if r.json()["result"]==False and "This email is already in use or its owner has excluded it from our website" in r.text:

  print(f"{email} ==>Exist In xvideos")

else:
  print(f"{email} ==>Not Exist in xvideos")
