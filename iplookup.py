import requests
# 設定查詢目前 ip 的 api 網址
url = 'https://api.ipify.org'
r = requests.get(url)
print('我目前的IP: ', r.text)