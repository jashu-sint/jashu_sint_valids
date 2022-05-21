import requests
h = {
"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; V2055 Build/RP1A.200720.012)",
"X-APP-VERSION": "510",
"X-PLATFORM": "5",
"Device-Id":"1DF01C95A3A1EFE94F8271A2C2EB0B76342B112A",
"Host": "api.unacademy.com",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip"}

d = {"email":"YOUR_EMAIL"}

r = requests.post("https://api.unacademy.com/v1/user/email_registered/", headers=h, data=d)
print(r.text)
