import urllib.request
url = 'http://www.baidu.com'
proxy_handle = {
    'http':'183.51.190.51:33913',
    'http':'122.193.245.44:9999'
}
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request)
print(response.read().decode('utf8'))
while 1:
    print(response.status)   
    if (response.status != 200):
        print('爬虫失败')
    break





import urllib.request
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = 'http://www.baidu.com'
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)
for item in cookie:
print(item.name,item.value)
filename = 'tom.txt'
cookie.save(filename=filename,ignore_discard=True,ignore_expires=True)
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('tom.txt')
print(cookie)
##############################################
try:
    a = 100
    b = 100
    a + b
except Exception as o:
    print(o)
else:
    print('lalalala')



