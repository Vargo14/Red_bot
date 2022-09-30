import sys
import prog
import time

tags = []
data = []
result  = {}
try:
    data, tags = prog.user_inf(open('users_id.txt')) # data[id, name]
except:
    e = sys.exc_info()[0]
    print(f"Error: {e}")
    input("Не получилось прочитать user_id")

uniqe_tags = list(set(tags))
print('Какие теги нужно использовать?')
n = 0
for i in uniqe_tags:
    print(str(n) + ' ' + i, sep=' ')
    n += 1
print(str(n) + ' ' + "Использовать все")
tag = int(input())

brk = int(input("Введите задержку между аккаунтами в секундах: "))


with open('Ссылки_на_посты.txt') as f:
    posts = list(map(lambda x: x.rstrip(), f.readlines()))
if tag == n:
    for post in posts:
        for id_, user in data:
            name_of_user = user
            user_id = id_
            print(f'Имя: {name_of_user}, Пост : {post}', end=' ')
            try:
                up, join = prog.upvote(user_id, post)
            except:
                e = sys.exc_info()[0]
                print(f"Error: {e}")
                input("Нажмите Enter чтобы продолжить")
            print(f'Upvote: {up}, Join: {join}\n')
            if name_of_user in result:
                tmp = result.get(name_of_user)
                tmp[0] += up
                tmp[1] += join
                result[name_of_user] = tmp
            else:
                result[name_of_user] = [up, join]
            time.sleep(brk)
else:
    users = []
    for i in range(len(tags)):
        if uniqe_tags[tag] == tags[i]:
            users.append(data[i])
    for post in posts:
        for id_, user in users:
            name_of_user = user
            user_id = id_
            print(f'Имя: {name_of_user}, Пост : {post}')
            try:
                up, join = prog.upvote(user_id, post)
            except:
                e = sys.exc_info()[0]
                print(f"Error: {e}")
                input("Нажмите Enter чтобы продолжить")
            else:
                print(f'Upvote: {up}, Join: {join}\n')
            if name_of_user in result:
                tmp = result.get(name_of_user)
                tmp[0] += up
                tmp[1] += join
                result[name_of_user] = tmp
            else:
                result[name_of_user] = [up, join]
            time.sleep(brk)
for name, i in result.items():
    print(f'Имя:{name} Upvote:{i[0]} Join: {i[1]}')

input('Нажмите Enter чтобы выйти')

