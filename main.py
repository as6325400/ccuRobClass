import requests
from bs4 import BeautifulSoup as bs
from tool import login
from tqdm import tqdm
from env import ROBCLASSLIST

Robclass = False
count = 0

classList = ROBCLASSLIST


while True:
    SESSIONID = login.getSession()
    count += 1
    print(count, end=" ")
    for i in tqdm(range(1, 150 + 1)):
        paylaod = classList[i % len(classList)]
        paylaod['session_id'] = SESSIONID
        response = requests.post("http://140.123.30.101/~ccmisp98/cgi-bin/class/Add_Course01.cgi", paylaod)
        response.encoding = 'UTF-8'
        val = bs(response.text, features='html.parser')
        ans = str(val.find_all('font'))
        if "錯誤" not in ans:
            print("Success")
            print(f"Use {count} Rounds and {i} Times")
            classList.pop(i % len(classList))
    print()
    if  len(classList) == 0:
        break