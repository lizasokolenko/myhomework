def open_text(name): 
    with open (name+'.txt', 'r', encoding ='utf-8') as f: 
    text=f.read() 
    ntext=text.lower() 
    words=ntext.split(' ') 
    for i,word in enumerate (words): 
        words[i]=word.strip('.,!?-') 
    return words 
def edwords(a): 
    ed=[] 
    edlist=int() 
    for i,word in enumerate (a): 
        if word.endswith('ed'): 
            ed.append(word) 
            edlist+=1 
        print ('Количество форм на -ed равно',str(edlist)) 
    return (ed) 
def iedwords(b): 
    iedlist=int() 
    for i,word in enumerate (b): 
        if word.endswith('ied'): 
            iedlist+=1 
        print ('Количество форм, образованных от глаголов на -у или -е равно',str(iedlist)) 
    return () 
def end(): 
    name=input('Введите название файла: ') 
    a=open_text(name) 
    b=edwords(a) 
    c=iedwords(b) 
    return (c) 
u=end()
