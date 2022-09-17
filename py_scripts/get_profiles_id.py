import requests as rq


with open("login.txt") as f:
    data = {
            'username': f.readline()[:-1],
            'password': f.readline()
    }
print(data)
r = rq.post(url = 'https://anty-api.com/auth/login', data= data);
headers = {
    "Authorization": r.json()['token']
}
if r.status_code == rq.codes.ok:
    print('Обновление')
    br_id = rq.get('https://anty-api.com/browser_profiles', headers=headers)
    with open('users_id.txt', 'w') as user_f:
        for i in br_id.json()['data']:
            if len(i['tags']) == 0:
                tag  = 'No_tags'
            else:
                tag = i['tags'][0]
            user_f.write(i['name']+'//'+ str(i['id'])+ '//' +  tag + '\n')

else:
    print(f'Не получилось подключится к anty-api: {r.status_code}')
    input('Нажмите Enter чтобы продолжить')
input('Обновлено')
