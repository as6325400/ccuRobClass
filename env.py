# 設定帳密資料等

USERID = ""
PASSWORD = ""
URL = "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/"
LOGINROUTER = "bookmark.php"
ROBCLASSROUTER = "Add_Course01.cgi"

# 多少次搶課後要重新登錄一次，預設150
ROUNDTIMES = 150

# 一秒送出多少次請求，預設三次，最多可到10次
TIMESINONESECOND = 2

# 這邊存想搶課程的payload
# session_id 在 main 拿
ROBCLASSLIST = [
    # 這堂是周二 2, 3 的星空探索
    {
        "session_id": "",
        "dept": "I001",
        "grade": "1",
        "cge_cate": "2",
        "cge_subcate": "6",
        "page": "2",
        "e": "0",
        "m": "0",
        "SelectTag": "1",
        "7500030_02": "3",
        "7501019_01": "3",
        "7502001_01": "3",
        "7502002_01": "3",
        "7503012_01": "3",
        "7505010_01": "3",
        "7506011_01": "3",
        "course": "7506012_01",
        "7506012_01": "3",
        "7506012_02": "3",
        "7506014_01": "3"
    }
]