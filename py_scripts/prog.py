import os
import json
import random
import requests as rq
import selenium as sl
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

cwd = os.getcwd()


def connecting_to_dolfin(user_id):
    try:
        r = rq.get(f'http://localhost:3001/v1.0/browser_profiles/{user_id}/start?automation=1')
        port = json.loads(r.content).get('automation').get('port')
    except:
        print('Не получилось подключится к dolphin. Возможно Dolphin Anty не запущен')
        input('')
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{port}")
    s = webdriver.chrome.service.Service(f"{cwd}/chromedriver-windows-x64.exe")
    driver = webdriver.Chrome(service=s, options=chrome_options)
    return driver

def user_inf(file):
    data = []
    tags = []
    with open('users_id.txt') as f:
        for i in f.readlines():
            name, id_, tg, = i.split('//')
            tags.append(tg[:-1])
            data.append([id_, name])
    return data, tags
def upvote(user_id, posts):
    joined = 0
    upvotes = 0
    one_post = False
    driver = connecting_to_dolfin(user_id)
    if isinstance(posts, str):
        one_post = True
        posts = [posts]
    for post in posts:
        inf_post = post
        if one_post:
            inf_post = ''
        driver.get(post)
        driver.implicitly_wait(4)
        try:
            driver.find_element(By.CSS_SELECTOR, 'div[data-test-id="post-content"] button[aria-label="upvote"][aria-pressed="false"]').click()
            upvotes += 1
        except sl.common.exceptions.NoSuchElementException:
            print(f'{inf_post} - Не получилось поставить апвоут. Возможно он уже поставлен.')
        driver.implicitly_wait(2)
        try:
            driver.find_element(By.CSS_SELECTOR, 'a[data-click-id="subreddit"]').click()
        except sl.common.exceptions.NoSuchElementException:
            driver.find_element(By.CSS_SELECTOR, 'span[title^= "r/"]').click()
            t
        driver.implicitly_wait(3)
        try:
            if driver.find_element(By.CSS_SELECTOR, 'div._1Q_zPN5YtTLQVG72WhRuf3  > button').text == "Join":
                driver.find_element(By.CSS_SELECTOR, 'div._1Q_zPN5YtTLQVG72WhRuf3  > button').click()
                joined += 1
            else:
                print(f'{inf_post} - Не удалось нажать Join, возможно уже засабан')
        except sl.common.exceptions.NoSuchElementException:
            print(f'{inf_post} - Не удалось найти Join, возможно уже засабан')
        driver.implicitly_wait(2)
    driver.implicitly_wait(random.randrange(1,5))
    rq.get(f'http://localhost:3001/v1.0/browser_profiles/{user_id}/stop')
    return upvotes, joined


# def scrolling(user_id):
#
#     driver = connecting_to_dolfin(user_id)
#
#     driver.get('https://www.reddit.com/')
#     clickable = driver.find_elements_by_id("vote-arrows-t3_xjmgy3")
#     for element in clickable:
#             element.
#     # action_chains.ActionChains(driver)\
#     #     .move_to_element(clickable)\
#     #     .pause(1)\
#     #     .click()\
#     #     .perform()
