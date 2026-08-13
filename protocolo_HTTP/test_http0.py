import requests
url= 'http://httpbin.io/'
r =requests.get(url)
print (r)
print(r.status_code)
print(r.headers)

