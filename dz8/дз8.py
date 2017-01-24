import random
def bigram():
    b={}
    with open ('text.csv', 'r') as f:
        lines=f.readlines()
        for line in lines:
            line=line.split(',')
            b[line[0]]=line[1]
    return(b)

def dots(w):
    res=''
    for i in range(len(w)):
        res+='. '
    return res

def rand(b):
    k=list(b.keys())
    return random.choice(k)

print ('Сейчас мы сыграем в игру "Угадай слово"!')
big=bigram()
word=rand(big)
print ("Подсказка:")
print (big[word]+' '+ dots(big[word]))
answer=input('Как вы думаете, что это за слово? ')
if answer==word:
             print ("Правильно!")
else:
             print ('Увы, неправильно!')
    
