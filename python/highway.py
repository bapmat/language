#https://blog.naver.com/kimnr123/221881864846](https://blog.naver.com/kimnr123/221881864846)

# import urllib.request
# import json

#import pandas as pd

# #한국도로공사 고속도로 공공데이터 포털
# url = 'http://data.ex.co.kr/openapi/safeDriving/forecast?key=test&type=json'
# req = urllib.request.Request(github_address, headers={
# "Authorization": github_token
# })
# res = urllib.request.urlopen(req)
# body = res.readline()

# j = json.loads(body)
# print(j)

######################################################

import requests

#한국도로공사 고속도로 공공데이터 포털
url = 'http://data.ex.co.kr/openapi/safeDriving/forecast?key=test&type=json'
rjson = requests.get(url)
result = rjson.json()

data = result['list']

for i in range(0, len(data)) :
    print(data[i])