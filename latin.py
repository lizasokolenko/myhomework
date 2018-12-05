#Выполнила Соколенко Елизавета 2 курс
#Задание: Albus/Candidus
#Убрать стоп-слова
#Найти биграммы с прилагательными “белый”
#Определить топ-10 существительных, сочетающихся с каждым из прилагательных
#Попытаться дать семантическое обоснование распределению
import os
import re
import re
from cltk.corpus.utils.importer import CorpusImporter
from cltk.lemmatize.latin.backoff import TrainLemmatizer
from cltk.stem.lemma import LemmaReplacer
from cltk.stem.latin.j_v import JVReplacer
import nltk
from collections import Counter

stop = ['ab', 'ac', 'ad', 'adhic', 'aliqui', 'aliquis', 'an', 'ante', 'apud', 'at', 'atque', 'aut', 'autem', 'cum',
              'cur', 'de', 'deinde', 'dum', 'ego', 'enim', 'ergo', 'es', 'est', 'et', 'etiam', 'etsi', 'ex', 'fio', 'haud',
              'hic', 'iam', 'idem', 'igitur', 'ille', 'in', 'infra', 'inter', 'interim', 'ipse', 'is', 'ita', 'magis', 'modo',
              'mox', 'nam', 'ne', 'nec', 'necque', 'neque', 'nisi', 'non', 'nos', 'o', 'ob', 'per', 'possum', 'post', 'pro',
              'quae', 'quam', 'quare', 'qui', 'quia', 'quicumque', 'quidem', 'quilibet', 'quis', 'quisnam', 'quisquam', 'quisque',
              'quisquis', 'quo', 'quoniam', 'sed', 'si', 'sic', 'sive', 'sub', 'sui', 'sum', 'super', 'suus', 'tam', 'tamen',
              'trans', 'tu', 'tum', 'ubi', 'uel', 'uero', 'unus', 'ut', 'qvi', 'qve,', 'qvam','qvae','qvam']
# Ниже проходимся по файлам, из-за того, что тексты большие, пришлось разделить их на несколько групп.
a = []
for elem in os.listdir()[5:9]:
    with open(elem, 'r', encoding='UTF-8') as t:
        for line in t.readlines():
            for word in line.split():
                a.append(word)
print(a)
line = ' '.join(a)
# Импортируем латинский корпус.
corpus_importer = CorpusImporter('latin')
lemmatizer = TrainLemmatizer(corpus_importer.import_corpus('latin_models_cltk'))
# Лемматизируем все тексты и убираем стоп-слова.
sentence = line.lower()
lemmatizer = LemmaReplacer('latin')
l = lemmatizer.lemmatize(sentence)
line1 = ' '.join(l)
t = []
for i in line1.split():
    if i in stop:
        continue
    else:
        t.append(i)
t = ' '.join(t)
# Делим слова на пары.
bigrm = list(nltk.bigrams(t.split()))
print (bigrm)
# Ищем слова, находящиеся слева и справа от интересующих нас слов.
for elem in bigrm:
    for i in elem:
        if i=='albus':
            result2.append(elem)
        if i=='candidus':
            result1.append(elem)
# Печатаем 10 самых частотных слов для "candidus". Для "albus" слишком мало биграмм.
c = {}
for el1 in result1:
    for word in el1:
        if word in c:
            c[word]+=1
        else:
            c[word]=1
Counter(c).most_common(20)

