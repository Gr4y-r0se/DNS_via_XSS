import json
from sys import argv
import base64

with open(argv[1],'r') as file:
    json = json.loads(file.read())

arry= []
values = eval(json['app'].replace('true','True').replace('false','False'))


for key in values['data']:
    arry.append(key['full-id'])
    

arry = [i.lower() for i in arry if len(i.split('.'))==4 ]
results = list(set(arry))


results.sort(key=lambda x: int(x.split('.')[0]))

ph = []

fill,exfil='',''
for i in results:
    _,a,b,_ = i.split('.')
    fill += a
    exfil += b

if len(exfil) < len(fill):
	exfil += '='*(len(fill) - len(exfil))

for i in range(len(exfil)):
	if fill[i] == '1' and exfil[i].isalpha():
		ph.append(exfil[i].upper())
	else:
		ph.append(exfil[i])

result = base64.b64decode(''.join(ph))

print(result.decode('utf-8'))
