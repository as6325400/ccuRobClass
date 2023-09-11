import sys
sys.path.append('../')  
import requests
from bs4 import BeautifulSoup as bs
from env import *

def getSession():
    response = requests.post(URL, data={"id" : USERID, "password" : PASSWORD})
    response.encoding = 'UTF-8'
    loginWeb = bs(response.text, features='html.parser')
    loginLog = loginWeb.title.string

    if loginLog == "主選單":
        sessionTag = loginWeb.find('meta', {'http-equiv': 'refresh'})

        if sessionTag != None:
            sessionTag = sessionTag.get('content')
            start_index = sessionTag.find('session')
            if start_index != -1:
                start_index += len('session_id=')
                return sessionTag[start_index:]
            else:
                print("Not found session_id")
                return False
    else:
        print(loginLog)
        return False
    

