import requests
from bs4 import BeautifulSoup as bs
from tool import login
from tqdm import tqdm

Robclass = False
count = 0

while True:
    SESSIONID = login.getSession()
    count += 1
    for i in tqdm(range(1, 150 + 1)):
        paylaod = {"session_id": SESSIONID,
                "dept" : "4104",
                "grade" : "3", 
                "e": "0",
                "m": "0",
                "SelectTag": "1",
                "4103001_01": "1",
                "4103001_02": "1",
                "4103022_01": "2",
                "course": "4103022_01",
                "4103026_01": "2",
                "4103055_01": "1",
                "4103055_02": "1",
                "4103800_01": "1"
                }
        
        response = requests.post("http://140.123.30.101/~ccmisp98/cgi-bin/class/Add_Course01.cgi", paylaod)
        response.encoding = 'UTF-8'
        val = bs(response.text, features='html.parser')
        ans = str(val.find_all('font'))
        if "錯誤" not in ans:
            Robclass = True
            break
    if Robclass == True:
        print("Success")
        print(f"Use {count} Rounds and {i} Times")
        break