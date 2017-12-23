import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('hittite.db')
c = conn.cursor()
conn_n = sqlite3.connect('NEW_DB.db')
c_n = conn_n.cursor()

c_n.execute('DROP TABLE IF EXISTS words')
c_n.execute('create table words(wordId INTEGER, lemma,wordform,gloss)')
c_n.execute('DROP TABLE IF EXISTS glosses')
c_n.execute('create table glosses(glossId INTEGER, value, transcript)')
c_n.execute('DROP TABLE IF EXISTS word_glosses')
c_n.execute('create table word_glosses (id_words INTEGER, id_glosses INTEGER)')

lemma = []
for raw in c.execute("""SELECT lemma FROM wordforms"""):
    lemma.append(raw)
wordforms = []
for raw in c.execute("""SELECT wordform FROM wordforms"""):
    wordforms.append(raw)
glosses = []
for raw in c.execute("""SELECT glosses FROM wordforms"""):
    glosses.append(str(raw).replace('.',' '))
for x in range(0, len(lemma)):
    print(x)
    c_n.execute('INSERT into words(wordId, lemma, wordform, gloss) values (?, ?,?,?)',((x+1), lemma[x][0], wordforms[x][0], glosses[x].split('\'')[1]))
    conn_n.commit()
data = []
data_1 = []
with open('Glossing_rules.txt', 'r', encoding='UTF-8') as t:
    H = t.readlines()
    for line in H:
        data.append(line.split('—')[0].strip())
        data_1.append(line.split('—')[1][:-1].strip())
for n in range(0, len(data)):
    c_n.execute('INSERT into glosses (glossId, value, transcript) values (?, ?, ?)',((n+1), data[n], data_1[n]))
    conn_n.commit()
data.remove('\ufeffADJ')
data.insert(0,'ADJ')
tab = []
dots_c = {}
parts_of_speech = {}
dots_v = {}
dots_n = {}
raws = list(c_n.execute("""SELECT wordId, gloss FROM words"""))
for raw in raws:
    try:
        glss = raw[1].split()
        glss.append('')
        st_sel = """SELECT glossId FROM glosses WHERE value IN {}""".format(tuple(glss))
        for raw2 in c_n.execute(st_sel):
            tab.append((raw[0],raw2[0]))
    except:
        continue
    for elem in glss:
        if elem in data[:19]:
            if elem in parts_of_speech:
                parts_of_speech[elem] += 1
            else:
                parts_of_speech[elem] = 1
        elif elem in data[20:29]:
            if elem in dots_c:
                dots_c[elem] += 1
            else:
                dots_c[elem] = 1
        elif elem in data[29:33]:
            if elem in dots_v:
                dots_v[elem] += 1
            else:
                dots_v[elem] = 1
        elif elem in data[33:35]:
            if elem in dots_n:
                dots_n[elem] += 1
            else:
                dots_n[elem] = 1


def plot_lib(vocab,lst):
    for n in range(0,len(vocab)):
        plt.title(lst[0])
        plt.xlabel(lst[1])
        plt.ylabel(lst[2])
        plt.scatter(n, list(vocab.values())[n])
        plt.text(n , list(vocab.values())[n] ,list(vocab)[n])
#n-просто номер по счету
    return plt.show()


plt.show(plot_lib(parts_of_speech,['Parts of speech','','Amt of words']))
plt.show(plot_lib(dots_c,['Cases','','Amt of words']))
plt.show(plot_lib(dots_v,['Forms of verbs','','Amt of words']))
plt.show(plot_lib(dots_n,['Number','','Amt of words']))
for el in tab:
    c_n.execute('INSERT into word_glosses (id_words, id_glosses) values (?,?)', (el[0], el[1]))
    conn_n.commit()
