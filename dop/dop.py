from flask import Flask
from flask import request
from flask import render_template, Response
import os
import urllib.request
import re
from pymystem3 import Mystem
from collections import Counter


app = Flask(__name__)
app.debug=True

d = {}
pattern = re.compile("'|,")
with open('new.tsv', 'r', encoding='UTF-8') as t:
    H = t.readlines()
    for line in H:
        try:
            new_word = line.split()[0]
            old_word_1 = line.split()[1]
            old_word = pattern.sub('', old_word_1)
            d[new_word] = old_word
        except (IndexError):
            pass


def vocab(word):
    r = re.compile("[а-яА-Я]+")
    glasn = ['а', 'и', 'у', 'э', 'ѣ', 'ы', 'е', 'ё', 'о', 'ю', 'я', 'ъ', 'ь', 'й', 'А', 'И', 'У', 'Э', 'Е', 'Ё', 'О', 'Я',
             '.', ',']
    word = word.lower()
    m = Mystem()
    if r.findall(word) is not None:
        try:
            res = m.analyze(word)
            value = res[0]['analysis'][0]['gr'].split(',')[0]
            lemma = res[0]['analysis'][0]['lex']
            if value == 'S':
                try:
                    rod = res[0]['analysis'][0]['gr'].split(',')[1]
                    pad = res[0]['analysis'][0]['gr'].split(',')[2].split('=')[1]
                    chisl = res[0]['analysis'][0]['gr'].split(',')[3]
                    if '(' in pad:
                        pad = res[0]['analysis'][0]['gr'].split(',')[2].split('=(')[1]
                        chisl = res[0]['analysis'][0]['gr'].split(',')[3].split('|')[0]
                    if (rod == 'жен' and (lemma[-1] == 'а' or lemma[-1] == 'я') and chisl == 'ед' and (
                        pad == 'дат' or pad == 'пр')) or (rod == 'муж' and (
                        lemma[-1] == 'ь' or lemma[-1] not in glasn) and chisl == 'ед' and pad == 'пр'):
                        n_word = word.replace(lemma[:-1], d[lemma][:-1])
                        print(n_word)
                        n_word = n_word[:-1] + 'ѣ'
                    elif rod == 'муж' and lemma[-1] not in glasn:
                        n_word = word.replace(lemma, d[lemma][:-1])
                    else:
                        n_word = word.replace(lemma[:-1], d[lemma][:-1])
                except:
                    n_word = word
            elif value == 'PR=' or value == 'PART=' or value == 'SPRO':
                n_word = word
            elif value == 'V':
                if 'ѣ' in d[lemma]:
                    n_word = word.replace('е', 'ѣ')
                elif 'ѳ' in d[lemma]:
                    n_word = word.replace('ф', 'ѳ')
                elif 'і' in d[lemma]:
                    n_word = word.replace('и', 'і')
                elif 'ѵ' in d[lemma]:
                    n_word = word.replace('в', 'ѵ')
                else:
                    n_word = word
            else:
                try:
                    n_word = d[word]
                except KeyError:
                    n_word = word
            if n_word[-1] not in glasn:
                n_word = n_word + 'ъ'
            if n_word[-2:] == 'іе':
                n_word = n_word.replace('іе', 'ія')
            if n_word[-2:] == 'ые':
                n_word = n_word.replace('ые', 'ыя')
            if n_word[-2:] == 'иеся':
                n_word = n_word.replace('иеся', 'іяся')
        except:
            n_word = word
    return n_word


@app.route('/')
def quest():
    T, weath = download_page_w('https://yandex.ru/pogoda/10463')
    return render_template('index.html', temperature=T, weather=weath)


@app.route('/newword')
def analize():
    word = request.args['word']
    return render_template('new.html',new_word=vocab(word))


@app.route("/test")
def test_page():
    return render_template('test.html', page_title='Тест')


def download_page(commonUrl):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request(commonUrl, headers = {'User-Agent': user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('windows-1251')
    pattern = re.compile('[а-яА-ЯёЁ]+', flags=re.DOTALL)
    article = pattern.findall(html)
    print(article)
    new_article = []
    for elem in article[:15]:
    #можно поставить любое число, смотря сколько времени вы хотите потратить....
        elem = vocab(elem)
        print(elem)
    # тут можно проследить как переводятся слова
        new_article.append(elem)
        article_new = ' '.join(new_article)
    count = Counter(x for x in re.findall(r'[а-яА-ЯёЁ|і|Ѣ]+', article_new))
    a = []
    for el in count.most_common(10):
        a.append('{}—{}'.format(el[0], el[1]))
        w = ', '.join(a)
    return article_new, w


@app.route('/thanks')
def th():
    prav = 0
    if request.args['a'] == '1_1':
        prav += 1
    if request.args['b'] == '1_1':
        prav += 1
    if request.args['c'] == '1_2':
        prav += 1
    if request.args['d'] == '1_2':
        prav += 1
    if request.args['e'] == '1_1':
        prav += 1
    if request.args['f'] == '1_2':
        prav += 1
    if request.args['g'] == '1_2':
        prav += 1
    if request.args['h'] == '1_2':
        prav += 1
    if request.args['i'] == '1_1':
        prav += 1
    if request.args['j'] == '1_1':
        prav += 1
    res = str(prav*10)
    return render_template('thanks.html', page_title='Спасибо',results = res)


def download_page_w(commonUrl_w):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request(commonUrl_w, headers={'User-Agent':user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')

    regWeather = re.compile('<span class="temp__value">.*?</span>',flags= re.DOTALL)
    Weather = regWeather.findall(html)
    T = Weather[0][26:-7]
    regWeather = re.compile('<div class="fact__condition day-anchor i-bem" data-bem=.*?>.*?</div>',flags= re.DOTALL)
    Weather = regWeather.findall(html)
    weath = Weather[0][Weather[0].index('>')+1:-6]
    return T, weath


@app.route("/m")
def hj():
    articl, w = download_page('https://www.kommersant.ru/')
    return render_template('main.html', art = articl, word = w)


if __name__ == "__main__":
    app.run()


