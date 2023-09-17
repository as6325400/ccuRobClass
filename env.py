# 設定帳密資料等

USERID = ""
PASSWORD = ""
URL = "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/"
LOGINROUTER = "bookmark.php"
ROBCLASSROUTER = "Add_Course01.cgi"

# 多少次搶課後要重新登錄一次，預設150
ROUNDTIMES = 150

# 一秒送出多少次請求，預設三次，最多可到10次
TIMESINONESECOND = 1000

# 這邊存想搶課程的payload
# session_id 在 main 拿
ROBCLASSLIST = [
    # 林妙香 四 2,3
    {
        "session_id": "F7HGqqPH9OYE8mWXN12Q2I5MBnZ5TVpw2492",
        "dept": "I001",
        "grade": "1",
        "cge_cate": "2",
        "cge_subcate": "4",
        "page": "2",
        "e": "0",
        "m": "0",
        "SelectTag": "1",
        "7404018_01": "3",
        "7404031_01": "3",
        "7406037_01": "3",
        "7406039_01": "3",
        "7407026_01": "3",
        "7407026_02": "3",
        "course": "7407027_01",
        "7407027_01": "3",
        "7407027_02": "3",
        "7407027_03": "3",
        "7407027_04": "3"
    }
]