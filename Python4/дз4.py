word = input('Введите слово: ')
for i in range(len(word) , 0, -1):
    print(word[i:] + word[:i])
