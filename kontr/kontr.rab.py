import re
with open ('text.xml','r',encoding='utf-8') as f:
    lines=0
    for line in f:
          if '</teiHeader>' in line:
              break
          elif '</teiHeader>' not in line:
              lines+=1
with open('file.txt','w',encoding = 'utf-8') as m:
    m=lines
print(m)
