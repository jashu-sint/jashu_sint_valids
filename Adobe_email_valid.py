import requests
import json
def adobe(email):
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-IMS-CLIENTID': 'adobedotcom2',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://auth.services.adobe.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }
  data = '{"username":"' +email+ '","accountType":"individual"}'
  r = requests.post(
            'https://auth.services.adobe.com/signin/v1/authenticationstate',
            headers=headers,
            data=data)
  if r.status_code == 200:
    print(f"{email} ==> Exist in ADOBE")
    r = r.json()
    headers['X-IMS-Authentication-State'] = r['id']
    params = {'purpose': 'passwordRecovery',}
    response = requests.get('https://auth.services.adobe.com/signin/v2/challenges',headers=headers,params=params).json()
    if "securityPhoneNumber" in response.keys():
      print("Security phone ==>", response["securityPhoneNumber"])
    if "secondaryEmail" in response.keys():
      print("Second Email ==>", response["secondaryEmail"])
 

  else:
    print(f"{email} ==> Not exist in ADOBE")
    
    
adobe("YOUR_EMAIL")
