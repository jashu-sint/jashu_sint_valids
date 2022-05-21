import requests
import json

email = ("YOUR_EMAIL")
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://hub.docker.com/signup',
        'Content-Type': 'application/json',
        'X-CSRFToken': '',
        'Origin': 'https://hub.docker.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

data = '{"email":"'+email+'","password":"","recaptcha_response":"","redirect_value":"","subscribe":true,"username":""}'

r = requests.post('https://hub.docker.com/v2/users/signup/', headers=headers, data=data)

if "This email is already in use." in r.text:
  print(f"{email} ==> Exists in DOCKER")
else:
  print(f"{email} ==> Not Exist in DOCKER")
