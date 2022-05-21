import requests
from random import randint

def check(email):
  url = "https://idmsac.apple.com/authenticate"

  ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(randint(10,100))+"."+str(randint(1,10))+"."+str(randint(1000,10000))+"."+str(randint(100,1000))+" Safari/537.36"
  params = {'accountPassword':'xxxx',
          'appleId':email,
          'appIdKey':'3b356c1bac5ad9735ad62f24d43414eb59715cc4d21b178835626ce0d2daa77d'
          }
  r = requests.post(url, data=params, headers={'User-Agent':ua})

  
  if "Your account information was entered incorrectly" in r.text:
    print(f"{email} ==> Not exists in APPLE")
  else:
    print(f"{email} ==> Exists in APPLE")


check("YOUR_EMAIL")
