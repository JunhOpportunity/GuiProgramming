from tkinter import PhotoImage
from urllib.request import urlopen
from urllib.parse import quote_plus
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import tkinter.messagebox as msgbox
import time

# 사진 가져오는 함수
def scrap_profile_img():
    # 브라우저를 열지 않고 작업 수행하기
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")

    # URL 입력. 이제 실제 FUNCTION 파일에서 사용할 때는 format을 이용해야겠디
    url = "{}".format(url_entry.get())
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    time.sleep(4)

    html = browser.page_source
    soup = BeautifulSoup(html)

    time.sleep(4)

    # class 검색 후 src 뒤의 text 가져오기
    insta = soup.select_one('._6q-tv')
    img_url = insta["src"]
    print(img_url)

    # 사진 저장하기
    with urlopen(img_url) as f:
        with open("testImg.jpg", "wb") as h:
            img = f.read()
            h.write(img)

    browser.close()

# Enter Button 구동 함수
def enter_btn_cmd():
    if len(url_entry.get()) == 0:
        # 경고창 (instagram url을 입력해주세요)
        msgbox.showerror("경고", "Instagram Url을 입력해주세요")
    else:
        scrap_profile_img()
        time.sleep(2)
        change_basic_img()
        time.sleep(2)
        response = msgbox.askyesno("예 / 아니오", "이 사진이 맞나요?") # response 전역변수로 설정해야하는데..

# 기본 사진을 스크랩 해온 사진으로 바꾸는 함수
def change_basic_img():
    change_img = PhotoImage(file="testImg.jpg")
    profile_label.config(image=change_img)

# 사진이 맞는지 확인하는 함수 (메세지 박스에서 예:1, 아니오:0)
def check_img():
    if response == 1:
        msgbox.showinfo("알림", "저장 경로를 설정해주세요.")
        # 메세지 박스로 저장 경로를 설정하세요.
        pass
    else:
        # 다시 basic 사진으로 변경 + url 입력 칸 초기화
        profile_img_label = PhotoImage(file="./instagram.png")
        profile_label.config(image=profile_img_label)
        


