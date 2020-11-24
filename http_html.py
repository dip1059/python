import requests
import hashlib
import re


url="http://165.232.39.143:32517/"
r=requests.session()
out=r.get(url)
out1=re.search("<h3 align='center'>(\w*)</h3>",out.text)
out11=hashlib.md5(out1.group(1).encode('utf-8')).hexdigest()
print("sending md5 :- {}".format(out11))

data={'hash': out11}
out = r.post(url=url, data=data)
print(out.text)
