import os
import json
import requests as rq
import selenium as sl
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

cwd = os.getcwd()

def upvote(user_id, posts):
    joined = 0
    upvotes = 0
    try:
        r = rq.get(f'http://localhost:3001/v1.0/browser_profiles/{user_id}/start?automation=1')
    except:
        print('Не получилось подключится к dolphin. Возможно Dolphin Anty не запущен')
        input('Нажмите Enter чтобы продолжить')
    port = json.loads(r.content).get('automation').get('port')

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{port}")
    s = webdriver.chrome.service.Service(f"{cwd}/chromedriver-windows-x64.exe")
    driver = webdriver.Chrome(service=s, options=chrome_options)

    for post in posts:
        #name_of_post =
        driver.get(post)
        driver.implicitly_wait(4)
        try:
            driver.find_element(By.CSS_SELECTOR, 'div[data-test-id="post-content"] button[aria-label="upvote"][aria-pressed="false"]').click()
            upvotes += 1
        except sl.common.exceptions.NoSuchElementException:
            print(f'{post} - Не получилось поставить апвоут. Возможно он уже поставлен.')
        driver.implicitly_wait(2)
        try:
            driver.find_element(By.CSS_SELECTOR, 'a[data-click-id="subreddit"]').click()
        except sl.common.exceptions.NoSuchElementException:
            driver.find_element(By.CSS_SELECTOR, 'span[title^= "r/"]').click()
        driver.implicitly_wait(3)
        try:
            if driver.find_element(By.CSS_SELECTOR, 'div._1Q_zPN5YtTLQVG72WhRuf3  > button').text == "Join":
                driver.find_element(By.CSS_SELECTOR, 'div._1Q_zPN5YtTLQVG72WhRuf3  > button').click()
                joined += 1
            else:
                print(f'{post} - Не удалось нажать Join, возможно уже засабан')
        except sl.common.exceptions.NoSuchElementException:
            print(f'{post} - Не удалось найти кнопку саба, возможно уже засабан')
        driver.implicitly_wait(2)

    rq.get(f'http://localhost:3001/v1.0/browser_profiles/{user_id}/stop')
    return upvotes, joined
