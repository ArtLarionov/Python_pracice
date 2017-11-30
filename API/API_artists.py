import requests
import json
from operator import itemgetter

client_id = "45346482f3f982c22a2d"
client_secret = "0454690c0c29af773f77659322570460"

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                            data={
                                "client_id": client_id,
                                "client_secret": client_secret
                            })
# разбираем ответ сервера
j = json.loads(r.text)

# получаем ответ сервера
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

with open('/Users/Artem/Desktop/dataset_24476_4.txt') as read_file, \
        open('/Users/Artem/Desktop/result_file.txt', 'w') as result_file:
    id_list = read_file.read().strip().split("\n")
    lst = []
    for ident in id_list:
        # инициируем запрос с заголовком
        api_url = "https://api.artsy.net/api/artists/{}".format(ident)
        req = requests.get(api_url, headers=headers)
        req.encoding = 'utf-8'

        # разбираем ответ сервера
        jsn = json.loads(req.text)
        name = jsn['sortable_name']
        birthday = jsn['birthday']
        res = (name, birthday)
        lst.append(res)

    new_lst = sorted(lst, key=itemgetter(1, 0))
    for elem in new_lst:
        result_file.write(elem[0] + '\n')
