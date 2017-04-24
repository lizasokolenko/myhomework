import os
letters=[]
s=''
for root, dirs, files in os.walk(' '):
    print (files)
    for i in files:
        letters.append(files)
        s=s+(files)

freq=[]
d={}
for i in letters:
    n=s.count(i)
    dic[i]=n

m=0
keymax=''
for key in d.keys():
    if d[key]>m:
        m=d[key]
        keymax=key
print ( 'Большинство файлов начинаются с ' + keymax+ '.')
