import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import datetime
from tool import login
from tqdm import tqdm
from env import *

Robclass = False
count = 0

classList = ROBCLASSLIST


import datetime
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup as bs
from time import sleep

count = 0
while True:
    SESSIONID = login.getSession()
    count += 1
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} {count} Rounds\n")
    for i in tqdm(range(1, ROUNDTIMES + 1)):
        sleep(1 / TIMESINONESECOND)
        paylaod = classList[i % len(classList)]
        paylaod['session_id'] = SESSIONID
        response = requests.post(URL + ROBCLASSROUTER, paylaod)
        response.encoding = 'UTF-8'
        val = bs(response.text, features='html.parser')
        ans = str(val.find_all('font'))
        if "錯誤" not in ans:
            with open("log.txt", "a") as log_file:
                log_file.write(f"Success to rob classID {classList[i % len(classList)]['course'][:-3]} on {datetime.datetime.now()}\n")
                log_file.write(f"Use {count} Rounds and {i} Times\n")
            classList.pop(i % len(classList))
            if len(classList) == 0:
                break
    if len(classList) == 0:
        break

