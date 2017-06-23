import re
import os
key_dict=[]
value_dict=[]
directory="C:\\Python33\\news"
for files in directory:
    f=os.listdir(directory) 
key_dict.append(f)
print(key_dict)
for files in os.listdir():
    with open(files,'r',encoding='cp1251') as text:
        text=text.read()
        a=re.findall('ana',text).count('ana')
        value_dict.append(a)
print(value_dict)
d = {}
for x, y in zip(key_dict, value_dict):
    d[x] = y

print (d)
with open('out.txt', 'w') as x:
    for key, value in d.items():     
             print (key, ":" , value)
             x.write(key+':'+str(value)+'\n')
x.close()
