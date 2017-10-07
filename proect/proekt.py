import os
import urllib.request
import re
import html.parser as prs

ROOT_PATH = 'C:\\MoscowNews\\'

def download_page(pageUrl):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request(pageUrl, headers={'User-Agent':user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')

    #заголовки
    regPostTitle = re.compile('<h1 class="material_title increase_text">.*?</h1>',flags= re.DOTALL)
    titles = regPostTitle.findall(html)
    title=titles[0][41:-5]
    #print(title)

##  дата
    regPostData = re.compile('<span><i class="black_clock"></i>.*?</span>',flags= re.DOTALL)
    dts = regPostData.findall(html)
    data = dts[0][39:-7]
    data=data.replace('/','.')
    #print(data)

    year=data[-4:]
    month=data[-6:-4]
    
##  автор
    regPostAuthor = re.compile('<meta name="author" content=".*?" >',flags= re.DOTALL)
    authors = regPostAuthor.findall(html)
    if len(authors) == 0:
        author = 'Noname'
    else:
        author=authors[0][29:-3]
    #print(author)
    
##  категория
    regPostCategory = re.compile('<title>.*?</title>',flags= re.DOTALL)
    categories = regPostCategory.findall(html)
    category = categories[0].split('|')[1].strip()
    #print(category)


##  адрес
    regPostAddress = re.compile('<meta property="og:url" content=".*?"',flags= re.DOTALL)
    addresses = regPostAddress.findall(html)
    address=addresses[0][33:-1]
    #print(address)

##  статья
    regArticle = re.compile('<article class="material_content increase_text">.*?</article>', flags=re.DOTALL)
    article=regArticle.findall(html)[0] 
    regTag = re.compile('<.*?>', re.DOTALL)  
    regScript = re.compile('<script>.*?</script>', re.DOTALL) 
    regComment = re.compile('<!--.*?-->', re.DOTALL) 
    article = regScript.sub("", article)
    article = regComment.sub("", article)
    article = regTag.sub("", article)
    article = prs.HTMLParser().unescape(article)
    article = article.strip()
    article='@au '+author+'\n'+'@ti '+title+'\n'+'@da '+data+'\n'+'@topic '+category+'\n'+'@url '+ address+'\n'+ article
    #print(article)

    #папки
    file_path = ROOT_PATH+'plain\\{}\\{}\\'.format(year, month)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_num = len(list(os.walk(file_path))[0][2])
    file_name = file_path + 'article{}.txt'.format(file_num+1)
    with open(file_name, 'w', encoding='utf-8') as fh:
        fh.write(article)

    #таблица
    row = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t%s\t\tнейтральный\
    \tн-возраст\tн-уровень\tрайонная\t%s\tМосковские Новости\
    \t\t%s\tгазета\tРоссия\tМосква\tru\n' % (file_path, author, title, data, category, address, year)

    with open(ROOT_PATH+'metadata.csv', 'a') as fh:
        fh.write(row)


    # файлы в mystem.txt
    file_path1=ROOT_PATH+'mystem-plain\\{}\\{}\\'.format(year,month)
    if not os.path.exists(file_path1):
        os.makedirs(file_path1)
    file_inp=ROOT_PATH+'plain\\{}\\{}\\article{}.txt\\'.format(year, month,file_num+1)
    file_out=ROOT_PATH+'mystem-plain\\{}\\{}\\article{}.txt'.format(year,month,file_num+1)
    os.system(r"C:\mystem.exe -id "+file_inp+' '+ file_out)


    # файлы в mystem.xml
    file_path2=ROOT_PATH+'mystem-xml\\{}\\{}\\'.format(year,month)
    if not os.path.exists(file_path2):
        os.makedirs(file_path2)
    file_inp1=ROOT_PATH+'plain\\{}\\{}\\article{}.txt\\'.format(year, month,file_num+1)
    file_out1=ROOT_PATH+'mystem-xml\\{}\\{}\\article{}.xml'.format(year,month,file_num+1)
    os.system(r"C:\mystem.exe -id "+file_inp1+' '+ file_out1)




f = open('metadata.csv', 'w')
f.close()

#скачивание страниц   
commonUrl = 'http://www.mn.ru/moscow/' 
for i in range(87543, 87600):
    pageUrl = commonUrl + str(i)
    download_page(pageUrl)







