import requests
import json

def git(email):
  x = requests.Session()
  a = x.get("https://github.com/join")
  token_regex = re.compile(
        r' {token}")
  data = {"value": email, "authenticity_token": token[0]}
  req = x.post("https://github.com/signup_check/email", data=data)
  if "Your browser did something unexpected." in req.text:
    print("Rate Limit")
  elif req.status_code == 422:
    print(f"{email} ==> Exist in GITHUB")
  elif req.status_code == 200:
    print(f"{email} ==> Not exist in GITHUB")
  else:
    print("Rate Limit")

git("YOUR_EMAIL")
