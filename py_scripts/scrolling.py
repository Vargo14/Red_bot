import prog
import sys


tags = []
data = []
try:
    data, tags = prog.user_inf(open('users_id.txt'))
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
users = data.copy()
if 0 <= n < tag:
    users = []
    for i in range(len(tags)):
        if uniqe_tags[tag] == tags[i]:
            users.append(data[i])

for user in
