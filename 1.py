import requests
import re
import time

sbor = open('2.txt', 'a')
list_email = open('list_email.txt', 'a')


def proverka(url):
    global i, k
    try:
        res = requests.get(url)
        if res.status_code == 200:
            print(url)
            url_contact = url
            url_text = requests.get(url_contact).text
            #      print(url_text)
            k = r'[\w_-]*@[\w_-]*\.[\w_-]*'  # поиск емейлов
            s = re.findall(k, url_text)  # список емейлов
            for j in s:
                list_email.write(j)
                list_email.write('\n')
            print(s)
            i = 'ok'
    #     exit()
    except:
        return


with open('1.txt') as f:
    for x in f:
        # получаем чистый домен
        k = r'https*://[w?]*\.?([\w\-\_]+\.\w*)+[/?]*'
        url2 = re.findall(k, x.strip())
        if len(url2) == 0:  # Проверка на пустую строку
            continue
        url = 'https://' + url2[0] + '/'
        #   print(url, end = '\t')
        i = 'no'
        w = open('contacts.txt')  # это окончания contacts
        for y in w:
            time.sleep(0.3)
            contact = y.strip()
            #     print(url + contact)
            try:
                proverka(url)
                if i == 'ok':
                    break
            except:
                continue

        if i == 'no':  # записываем, если не найдена страничка
            sbor.write(url)
            sbor.write('\n')
            print(url)
            proverka(url)
