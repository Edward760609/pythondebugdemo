from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


import ssl
ssl.create_default_context = ssl._create_unverified_context

page = 51
while True:
    #使用Beautifulsoup分析網頁原始碼
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    print("處理url:", url)
    #與if else相反 try except 可再丟出指令後針對回傳錯誤中止
    try:
        response = urlopen(url)
    except HTTPError:
        print("last page")
        break
    html = BeautifulSoup(response)
    #print(html)

    #find(找第一個符合條件的) find_all(找所有符合條件的)
    for r in html.find_all("li", class_="list-rst"):
    #print(html.find_all("li", {"class":"list-rst"})) 第二種寫法
        ja = r.find("small", class_ = "list-rst__name-ja")
        en = r.find("a", class_ = "list-rst__name-main")
        ratings = r.find_all("b", class_ = "c-rating__val")
        #萃取文字 .text 萃取特徵["特徵"]
        print(ratings[0].text,
              ja.text,
              en.text,
              en["href"])
    # 讓所有動作跑完最後在加count
    page = page + 1