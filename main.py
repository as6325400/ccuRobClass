import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import datetime
from tool import login
from tqdm import tqdm
from env import *
import os
import threading

Robclass = False
count = 0

classList = ROBCLASSLIST

def robclass(times):
    for i in range(1, times):
        paylaod = classList[i % len(classList)]
        paylaod['session_id'] = SESSIONID
        response = requests.post(URL + ROBCLASSROUTER, paylaod)
        response.encoding = 'UTF-8'
        val = bs(response.text, features='html.parser')
        ans = str(val.find_all('font'))
        # print(ans)
        if "錯誤" not in ans:
            print(ans)
            with open("log.txt", "a") as log_file:
                log_file.write(f"Success to rob classID {classList[i % len(classList)]['course'][:-3]} on {datetime.datetime.now()}\n")
                log_file.write(f"Use {count} Rounds and {i} Times\n")
            classList.pop(i % len(classList))
            if len(classList) == 0:
                break


while True:
    SESSIONID = login.getSession()
    CPUNUM = os.cpu_count()
    count += 1
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} {count} Rounds\n")
    # 開啟 mutithreads
    threads = []
    times = ROUNDTIMES // CPUNUM
    for i in range(1):
        thread = threading.Thread(target=robclass, args=(times, ), name=f"Thread-{i}")
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    if len(classList) == 0:
        break

