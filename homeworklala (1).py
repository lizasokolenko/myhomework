
# coding: utf-8

# In[3]:


import urllib.request
import ssl
import json


# In[4]:


post = []
count_dict=[]
users={}
comments = []
comm = []


# In[ ]:



post.clear()
comments.clear()
for n in range(4):
    num = 100*n
    line = 'https://api.vk.com/method/wall.get?owner_id=-63731512&count=100&offset={}&v=5.73&access_token=be471ab6be471ab6be471ab67ebe2593e8bbe47be471ab6e49a9a28a6647ea8ba8ce485'.format(num)
    req = urllib.request.Request(line)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
#     print(data)
    for i in range(99):
        try:
            if data['response']['items'][i]['text'] != None and data['response']['items'][i]['comments']['count'] < 100:
                post.append(data['response']['items'][i]['text'])
#                 print(post)
                leng=len(post[i].split())
                numb=data['response']['items'][i]['comments']['count']
                post_id = data["response"]["items"][i]["id"]
                line_1 = 'https://api.vk.com/method/wall.getComments?owner_id=-63731512&count={}&post_id={}&v=5.73&access_token=be471ab6be471ab6be471ab67ebe2593e8bbe47be471ab6e49a9a28a6647ea8ba8ce485'.format(numb,post_id)
                req_1 = urllib.request.Request(line_1)
                response_1 = urllib.request.urlopen(req_1)
                result_1 = response_1.read().decode('utf-8')
                data_1 = json.loads(result_1)
#                 print(data_1)
                for g in range(numb):
                    com = data_1["response"]["items"][g]["text"]
                    comm.append(data_1["response"]["items"][g]["text"])
                    if len(com)==0:
                        continue
#                     print(data_1["response"]["items"][g]['from_id'])
                    user = data_1['response']['items'][g]['from_id']
                    users[user]=len(com.split())
                    if 'id' in com:
                        com = com.split('],')[1]
                    comments.append(len(com.split()))
                aver = sum(comments) // len(comments)
                count_dict.append([aver, leng])
                print(users)
#                 print(count_dict)
            else:
                pass
        except:
            pass
f = open('text.txt', 'w')
f.write(post)
f.write(comm)
f.close()


# In[ ]:


import matplotlib.pyplot as plt

for r in count_dict:
    plt.scatter(r[1], r[0])
plt.xlabel('Длина поста(в словах)')
plt.ylabel('Средняя длина комментария(в словах)')
plt.savefig('posts_comments.png',format='png',dpi=100)
plt.show()


# In[ ]:


cities={}
i=0
for user in users:
    if i > 600:
        break
    if '-' in str(user):
        continue
    c_req = urllib.request.Request('https://api.vk.com/method/users.get?v=5.23&user_ids={}&fields=home_town'.format(str(user)))
    c_response = urllib.request.urlopen(c_req)
    city_result = c_response.read().decode('utf-8')
    city_data = json.loads(city_result) 
#     print (city_data['response'][0])
    if 'home_town' not in (city_data['response'][0]):
        continue
    cities[city_data['response'][0]['home_town']]=users[user]
    i+=1
print(cities)
    


# In[ ]:


id_cities={}
for city in cities:
    if city not in id_cities:
        id_cities[city]=[cities[city]]
    else:
        id_cities[city].append(cities[city])
print(id_cities)


# In[ ]:


import matplotlib.pyplot as plt

for p in id_cities:
    plt.bar(p, sum(id_cities[p])//len(id_cities[p]))
plt.xlabel('Город')
plt.ylabel('Средняя длина комментария(в словах)')
plt.xticks(rotation=90)
plt.savefig('cities_comments.png',format='png',dpi=100)
plt.show()


# In[ ]:


ages={}
i=0
for user in users:
    if i > 600:
        break
    if '-' in str(user):
        continue
    age_req = urllib.request.Request('https://api.vk.com/method/users.get?v=5.23&user_ids={}&fields=bdate'.format(str(user)))
    age_response = urllib.request.urlopen(age_req)
    age_result = age_response.read().decode('utf-8')
    age_data = json.loads(age_result) 
    print(age_data)
    if 'bdate' in age_data['response'][0]:
        try:
            age = 2018 - int(ages['response'][0]['bdate'].split('.')[2])
        except:
            continue
        ages[age]=users[user]
        print(age)
    
id_ages={}
for ag in ages:
    if ag not in id_ages:
        id_ages[ag]=[ages[ag]]
    else:
        id_ages[ag].append(ages[ag])
print(id_ages)


# In[ ]:


import matplotlib.pyplot as plt

for m in id_age:
    plt.scatter(m, sum(id_age[m])//len(id_age[m]))
plt.xlabel('Возраст')
plt.ylabel('Средняя длина комментария(в словах)')
plt.savefig('age_comments.png',format='png',dpi=100)
plt.show()


# In[ ]:



