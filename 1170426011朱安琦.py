def function_name
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'wd':'海绵宝宝'},encoding='utf8')
print(data)
ur1='http://www.baidu.com/s?'+data
print(ur1)
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)

data = bytes(urllib.parse.urlencode({'pw':'753','un':'456'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
print(result)