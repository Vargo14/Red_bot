import sys
import prog
import time
import traceback

tags = []
data = []
result  = {}
errors = []
try:
    data, tags = prog.user_inf(open('users_id.txt')) # data[id, name]
except:
    e = sys.exc_info()[0]
    print(f"Error: {e}")
    input("Не получилось прочитать user_id")

mode = input("Выберите режим: \n0 - пройтись профилями по одной ссылке \n1 - пройтись ссылками по одному профилю\n")
uniqe_tags = sorted(list(set(tags)))
print('Какие теги нужно использовать?')
n = 0
for i in uniqe_tags:
    print(str(n) + ' ' + i, sep=' ')
    n += 1
print(str(n) + ' ' + "Использовать все")
tag = int(input())

brk = int(input("Введите задержку между аккаунтами в секундах: "))
if brk < 0: brk = 0

try:
    with open('Ссылки_на_посты.txt') as f:
        posts = list(map(lambda x: x.rstrip(), f.readlines()))
except Exception as e:
    print(f'Error: {e} \nНе удалось открыть Ссылки на посты')
    input()
    exit()

if mode == '1':
    posts = [posts]
if tag == n:
    users = data
else:
    users = []
    for i in range(len(tags)):
        if uniqe_tags[tag] == tags[i]:
            users.append(data[i])

for post in posts:
    for id_, user in users:
        up, join = 0, 0
        name_of_user = user
        user_id = id_
        if post is str:
            print(f'Имя: {name_of_user}, Пост : {post}', end=' ')
        else:
            print(f'Имя: {name_of_user}')
        try:
            up, join = prog.upvote(user_id, post, brk)
        except Exception as e:
            print(f"Error: {e} ")
            print(traceback.format_exc())
            errors.append([name_of_user, post, e])
            continue
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
print('\nErrors:')
if errors:
    for nm, pst, er in errors:
        print(f'{nm}, {pst}\n {er}')
else:
    print('No errors\n')

input('Нажмите Enter чтобы выйти')

