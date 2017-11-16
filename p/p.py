from flask import Flask
from flask import request


def vocab():
    with open 'text.tsv' as t:
        for line in t:
            lang = line.split()[0]
            k = line.split()[1:]
        d = {[lang] }

        
app = Flask(__name__)

@app.route('/')
def index():
    return '<html><head><meta charset="utf-8"><title>Вопрос</title</head><body><form action=""><p><b> Введите язык: </b><input type="text" name="username" value=""></p></p><p><input type="submit"></p></form></body></html>'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/login')
def login(d):
    if request.args[''] == '':
        return 'Name: ' + request.args['login']
