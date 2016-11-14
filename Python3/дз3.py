word= 'сыр'
inf_list=[]
n_in_list=0
while word !='':
    word=input('Введите слово: ')
    if word[-2:] =='re' or word[-2:] == 'ri' or  word[-3:] == 'sse':
        inf_list.append(word)
        n_in_list += 1
for i in range (n_in_list):
    print(inf_list[i])
