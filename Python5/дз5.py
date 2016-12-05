with open("text.txt", "r", encoding="utf-8") as f: 
    text=f.read() 
words=text.split(' ') 
words_num=len(words) 
letters=list(text) 
marks_num=int() 
for i in letters: 
    if i=="." or i==",": 
        marks_num+=1
    percent=marks_num/words_num*100 
print('Процент слов, имеющих знак препинания: ', round(percent))
