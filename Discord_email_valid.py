import string
import requests
import random
import json

def random_str(l):
  letters = string.ascii_lowercase
  resu = ''.join(random.choice(letters) for i in range(l))
  return(resu)

email = input("Enter the email: ")


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
  'Accept': '*/*',
  'Accept-Language': 'en-US',
  'Content-Type': 'application/json',
  'Origin': 'https://discord.com',
  'DNT': '1',
  'Connection': 'keep-alive',
  'TE': 'Trailers'}

data = '{"fingerprint":"","email":"' + str(email) + '","username":"' + random_str(18) + '","password":"' + random_str(18) + '","invite":null,"consent":true,"date_of_birth":"","gift_code_sku_id":null,"captcha_key":null}'

a = requests.post('https://discord.com/api/v8/auth/register',headers=headers,data=data).json()
try:
  if "code" in a.keys():
    if a["errors"]["email"]["_errors"][0]["code"] == "EMAIL_ALREADY_REGISTERED":
      print(f"{email} ==> exist in DISCORD")
    else:
      print(f"{email} ==> Not exist in DISCORD")
  else:
    print(f"{email} ==> Not exist in DISCORD")
except:
  print(f"{email} ==> Not exist in DISCORD")
