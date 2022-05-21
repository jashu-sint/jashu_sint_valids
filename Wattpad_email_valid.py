import requests
import json

def wattpad(email):
  x = requests.Session()
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
     'Referer': 'https://www.wattpad.com/',
     'TE': 'Trailers'}
  try:
    a = x.get("https://www.wattpad.com", headers=headers)
    headers["X-Requested-With"] = 'XMLHttpRequest'
  except:
    print("Rate Limit")

  p = {'email': email}
  b = x.get("https://www.wattpad.com/api/v3/users/validate", headers=headers, params=p)
  if (b.status_code == 200 or b.status_code == 400):
    if "Cette adresse" not in b.text or b.text == '{"message":"OK","code":200}':
      print(f"{email} ==> Not exist in WATTPAD")
    else:
      print(f"{email} ==> Exist in WATTPAD")
  else:
    print("Rate Limit")

wattpad("YOUR_EMAIL")
