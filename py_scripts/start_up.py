import requests as rq
import re
import sys
import selenium as sl
import pandas as pd
import prog

tags = []
data = []
try:
    with open('users_id.txt') as f:
        for i in f.readlines():
            name, id_, tg, = i.split('//')
            tags.append(tg[:-1])
            data.append([id_, name])
except:
    e = sys.exc_info()[0]
    print(f"Error: {e}")
    input("Не получилось прочитать user_id")
uniqe_tags = list(set(tags))
result  = []

print('Какие теги нужно использовать?')
n = 0
for i in uniqe_tags:
    print(str(n) + ' ' + i, sep=' ')
    n += 1
print(str(n) + ' ' + "Использовать все")

tag = int(input())

with open('Ссылки_на_посты.txt') as f:
    posts = list(map(lambda x: x.rstrip(), f.readlines()))
    if tag == n:
        for id_, user in data:
            name_of_user = user
            user_id = id_
            print(f'Имя: {name_of_user}, id профиля: {user_id}')
            up, join = prog.upvote(user_id, posts)
            print(f'Upvote: {up}, Join: {join}\n')
            result.append([name_of_user, up, join])
    else:
        users = []
        for i in range(len(tags)):
            if uniqe_tags[tag] == tags[i]:
                users.append(data[i])
        for id_, user in users:
            name_of_user = user
            user_id = id_
            print(f'Имя: {name_of_user}, id профиля: {user_id}')
            up, join = prog.upvote(user_id, posts)
            print(f'Upvote: {up}, Join: {join}\n')
            result.append([name_of_user, up, join])
for i in result:
    print(f'Имя:{i[0]} Upvote:{i[1]} Join: {i[2]}')

input('Нажмите Enter чтобы выйти')

