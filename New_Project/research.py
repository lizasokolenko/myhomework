from flask import Flask
from flask import request
from flask import render_template
import json
import os.path
app = Flask(__name__)
filename = 'data.dat'

@app.route("/")
def hello():
    return render_template('index.html',  page_title='Анкета')

@app.route('/login')
def login():
    json_st = json.dumps(request.args)
    print(json_st)
    if not os.path.isfile(filename):
        fh = open(filename, 'w', encoding ='UTF-8')
        json.dump([], fh)
        fh.close()
    with open('data.dat', 'r', encoding='UTF-8') as fh:
        data_lst = json.load(fh)
        data_lst.append(request.args)
    with open('data.dat', 'w', encoding='UTF-8') as fh:
        json.dump(data_lst, fh, ensure_ascii=False)
    return render_template('thanks.html', page_title='Спасибо', name = request.args['name'])

@app.route("/stats")
def stats_page():
    d = {}
    num_words = {'paket': {'pak': 0, 'mesh': 0}, 'lav': {'lavk': 0, 'skam': 0}, 'sharf': {'shar': 0, 'plat': 0},
                 'slan': {'sl': 0, 'shl': 0}, 'vesh': {'veshal': 0, 'plech': 0}, 'fiol': {'fiolet': 0, 'lilov': 0},
                 'resin': {'res': 0, 'lastic': 0}, 'zmeika': {'zm': 0, 'mol': 0}}
    trans = {'pak': 'Пакет', 'mesh': 'Мешок', 'lavk': 'Лавка', 'skam': 'Скамейка', 'shar': 'Шарфик',
             'plat': 'Платок',
             'sl': 'Сланцы', 'shl': 'Шлепки', 'veshal': 'Вешалка', 'plech': 'Плечики', 'fiolet': 'Фиолетовый',
             'lilov': 'Лиловый', 'res': 'Резинка', 'lastic': 'Ластик', 'zm': 'Змейка', 'mol': 'Молния'}
    with open('data.dat', 'r', encoding='UTF-8') as fh:
        data_lst = json.load(fh)
        for data in data_lst:
            try:
                for key in num_words.keys():
                    num_words[key][data[key]] += 1
            except:
                pass
    words = []
    for key in num_words.keys():
        for word in num_words[key].keys():
            words.append(trans[word] + ' — ' + str(num_words[key][word]))
    return render_template('stats.html', page_title='Статистика',num=str(len(data_lst)), words=words)



@app.route("/search")
def search_page():
    return render_template('search.html', page_title='Поиск')

@app.route("/results")
def result_page():
    d = {}
    num_words = {'paket': {'pak': 0, 'mesh': 0}, 'lav': {'lavk': 0, 'skam': 0}, 'sharf': {'shar': 0, 'plat': 0},
                 'slan': {'sl': 0, 'shl': 0}, 'vesh': {'veshal': 0, 'plech': 0}, 'fiol': {'fiolet': 0, 'lilov': 0},
                 'resin': {'res': 0, 'lastic': 0}, 'zmeika': {'zm': 0, 'mol': 0}}
    trans = {'pak': 'пакет', 'mesh': 'мешок', 'lavk': 'лавка', 'skam': 'скамейка', 'shar': 'шарфик', 'plat': 'платок',
             'sl': 'сланцы', 'shl': 'шлепки', 'veshal': 'вешалка', 'plech': 'плечики', 'fiolet': 'фиолетовый',
             'lilov': 'лиловый', 'res': 'резинка', 'lastic': 'ластик', 'zm': 'змейка', 'mol': 'молния'}
    with open('data.dat', 'r', encoding='UTF-8') as fh:
        data_lst = json.load(fh)
        for data in data_lst:
            try:
                for key in num_words.keys():
                    num_words[key][data[key]] += 1
            except:
                pass
    words = {}
    for key in num_words.keys():
        for word in num_words[key].keys():
            words[trans[word]] = num_words[key][word]
    sex = {'male': 0, 'female':0}
    educ = {'nsec' : 0, 'sec' : 0, 'nhi' : 0, 'hi' : 0}
    tr = {'male':'мужского', 'female':'женского'}
    tr1 = {'nsec' : 'неоконченным средним', 'sec' : 'средним', 'nhi' : 'неоконченным высшим', 'hi' : 'высшим'}
    for elem in data_lst:
        if elem['sex'] == 'male':
            sex['male'] += 1
        else:
            sex['female'] += 1

    for elem in data_lst:
        if elem['educ'] == 'nsec':
            educ['nsec'] += 1
        elif elem['educ'] == 'sec':
            educ['sec'] += 1
        elif elem['educ'] == 'nhi':
            educ['nhi'] += 1
        else:
            educ['hi'] += 1
    for el in request.args['word']:
        try:
            el = str(words[request.args['word']])
        except KeyError:
            el = 'Нет данных'
    return render_template('results.html', page_title='Результаты поиска', sex=str(tr[request.args['sex']]),
                           sex_num = str(sex[request.args['sex']]), edu_type=str(tr1[request.args['educ']]),
                           edu_num=str(educ[request.args['educ']]), word=request.args['word'], word_num=el)

@app.route("/json")
def json_page():
    if not os.path.isfile(filename):
        return render_template('json_data.html', page_title='Json', json_data='No Data')
    with open('data.dat', 'r', encoding='UTF-8') as p:
        return render_template('json_data.html', page_title='Json', json_data = p.read())

if __name__ == "__main__":
    app.run()
