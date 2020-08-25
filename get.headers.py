import requests 
url = 'http://irs.thsrc.com.tw/IMINT'

headers= {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
# 將自訂的表頭加入 get 請求中
r = requests.get(url, headers = headers)
print(r)