import requests

headers = {
 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
print(HTML)
lines = HTML.split('\r\n')
print(lines)

for url in lines:
    try:
        response = requests.get(url,timeout=2)
        content = response.content
        conten2 = str(content)
        if '\\x' in conten2:
            print(conten2)
    except Exception as e:
        print(e)
        name = url.split('/')[-1]
        with open(name,'wb') as f:
            f.write(content)


              import requests
url = 'http://www.baidu.com/s?'
URLS = []
def baidu(wds):
    count = 1
    for wd in wds:
        res = requests.get(url,params={'wd':wd})
        path = 'res%d.txt'%count
        with open(path,'w',encoding='utf8') as f:
            f.write(res.text)
        count +=1
    print(wds)
if __name__ == "__main__":
    wds = ('哈哈','嘻嘻','呵呵')
    baidu(wds)
lines = res.split('\n')
for line in lines:
    if '(http' in line:
        split_ line.split('(http=')
        for i in split_:
            if 'http' in i or 'https' in i:
                res = i.split('png)')[1]
                if 'png' in res:
                    URLS.append(res)

for res in URLS:
    response = request.get(res)
    content = response.content
    name = res.split('/')[-1]
    with open(name,'wb')as f:
        f.write(conent)