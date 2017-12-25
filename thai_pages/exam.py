from flask import Flask
from flask import request
import os
import urllib.request
import re

path = 'C:\\Users\\lizas\\PycharmProjects\\thai_pages\\'

app = Flask(__name__)
app.debug=True


def files(path):
    for elem in os.listdir(path)[:-1]:
        with open(elem, 'r', encoding='UTF-8') as t:
            t = t.read()
            link = re.compile('<link rel="canonical" href="http://www.thai-language.com/let/.*?" />')
            l = link.findall(t)[0][28:-5]
            f = download_page(l)
    return f

TWords=[]
EWords=[]
def download_page(commonUrl):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request(commonUrl, headers = {'User-Agent': user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('UTF-8')
    # print(html)
    regThaiWord = re.compile('<a href=\'/let/.*\'>.*</a></span> •')
    regEngWord = re.compile('<td>.*?</td>')
    ThaiWords = regThaiWord.findall(html)
    EngWords = regEngWord.findall(html)
    print (EngWords)
    for el in EngWords[0].split('\','):
        # print (el)
        EWords.append(el[4:-5])
    print(EWords)
    for elem in ThaiWords[0].split('<a href='):
        # print(elem.split('•'))
        TWords.append(elem.split('•')[0][13:-12].replace('>',''))
    print(TWords)
    return TWords, EWords

print(files(path))

d = {}
d_1 = {}
filename = 'data.d'
def vocab(thai, eng ):

    for n in range[0,len(thai)]:
        try:
            d[eng[n]] = thai[n]
        except:
            pass
    for n in range[0,len(thai)]:
        try:
            d_1[thai[n]] = eng[n]
        except:
            pass

    if not os.path.isfile(filename):
        fh = open(filename, 'w', encoding ='UTF-8')
        json.dump([], fh)
        fh.close()
    with open('data.d', 'r', encoding='UTF-8') as fh:
        data_lst = json.load(fh)
        data_lst.append(d)
    with open('data.d', 'w', encoding='UTF-8') as fh:
        json.dump(data_lst, fh, ensure_ascii=False)

    if not os.path.isfile(filename):
        fh = open(filename, 'w', encoding ='UTF-8')
        json.dump([], fh)
        fh.close()
    with open('data.d', 'r', encoding='UTF-8') as fh:
        data_lst = json.load(fh)
        data_lst.append(d_1)
    with open('data.d', 'w', encoding='UTF-8') as fh:
        json.dump(data_lst, fh, ensure_ascii=False)

vocab(TWords, EWords)
@app.route("/")
def q():
    with open('quest.txt', 'r') as p:
        return p.read()

@app.route('/newword')
def analize():
    word = request.args['word']
    return d[word]



if __name__ == "__main__":
    app.run()