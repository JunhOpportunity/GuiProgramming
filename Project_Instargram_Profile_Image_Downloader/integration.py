from tkinter import PhotoImage
from urllib.request import urlopen
from urllib.parse import quote_plus
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import tkinter.messagebox as msgbox
from tkinter import filedialog
import time
import tkinter.ttk as ttk
from tkinter import *
from urllib import request
from PIL import Image
import os
from os import remove


response = 0


##########################################################################################################

# 셀레니움 스크래핑
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

    # 얻은 url로 접속 후 스크린샷
    browser.get(img_url)
    browser.get_screenshot_as_file("screenshottest.png")
    browser.close()

    time.sleep(3)
    
    # 사진 자르고 저장
    img_modify = Image.open("screenshottest.png")
    global cropped_img
    cropped_img = img_modify.crop((885, 465, 1035, 615))
    cropped_img.save("testimage.png")


##########################################################################################################
# 각종 함수들
# 기본 사진을 스크랩 해온 사진으로 바꾸는 함수
# 문제 1. 다운로드한 사진으로 안바뀜. 2. 다운로드한 사진을 찾을 수 없다고나옴
# 3. 근데 원래 있던 사진들은 아무 문제없이 실시간 변경
def change_basic_img():
    global change_img
    change_img = PhotoImage(file="./testimage.png")
    profile_label.config(image=change_img)

# 사진이 맞는지 확인하는 함수 (메세지 박스에서 예:1, 아니오:0)
def check_img(response):
    if response == 1:
        # 메세지 박스로 저장 경로를 설정하세요.
        msgbox.showinfo("알림", "저장 경로를 설정해주세요.")
        
    else:
        # 다시 basic 사진으로 변경 + url 입력 칸 초기화
        global profile_img_label
        profile_img_label = PhotoImage(file="./instagram.png")
        profile_label.config(image=profile_img_label)
        url_entry.delete(0, END)
        remove("screenshottest.png")
        remove("testimage.png")

# 저장 경로(folder)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':   # 사용자가 취소 누른 경우
        return
    url_entry.delete(0, END)
    url_entry.insert(0, folder_selected)

# download 
def download():
    # 파일 목록 확인
    if len(url_entry.get()) == 0:
        msgbox.showerror("경고", "Instagram Url을 입력해주세요")
        return
    
    # 저장 경로 확인
    if len(path_entry.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return
    
    # 문제 없을 시 다운로드 실행

# Enter Button 구동 함수
def enter_btn_cmd():
    if len(url_entry.get()) == 0:
        # 경고창 (instagram url을 입력해주세요)
        msgbox.showerror("경고", "Instagram Url을 입력해주세요")
    else:
        scrap_profile_img()
        time.sleep(4)
        change_basic_img()
        time.sleep(2)
        response = msgbox.askyesno("예 / 아니오", "이 사진이 맞나요?") # response 전역변수로 설정해야하는데..
        check_img(response)

# 저장 경로(folder)
def download_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':   # 사용자가 취소 누른 경우
        return
    path_entry.delete(0, END)
    path_entry.insert(0, folder_selected)

# download button
def download_button_click():
    file_name = "profile_image.{}".format(save_combobox.get())
    dest_path = os.path.join(path_entry.get(), file_name)
    cropped_img.save(dest_path)
    remove("screenshottest.png")
    remove("testimage.png")

##########################################################################################################

# 프레임

root = Tk()
root.title("Instargram Profile Image Downloader")
root.geometry()

# URL 입력 (entry, button)
url_frame = LabelFrame(root, text="Instargram URL")
url_frame.pack()

url_entry = Entry(url_frame, width=70)
url_entry.pack(padx=5, pady=5, side="left")


url_check_button = Button(url_frame, text="ENTER", command=enter_btn_cmd)
url_check_button.pack(padx=5, pady=5, side="right")

# Profile Image 확인할 수 있는 이미지 레이블 (label)
profile_img_frame = LabelFrame(root, text="Image")
profile_img_frame.pack(pady=20)

profile_img_label = PhotoImage(file="./instagram.png") # 사진 파일을 가장 바깥 폴더에 넣어야 찾을 수 있다고 나온다.
profile_label = Label(profile_img_frame, image=profile_img_label)
profile_label.pack(padx=10, pady=10)

# 저장 경로 설정 (entry, button)
download_frame = LabelFrame(root, text="저장 경로")
download_frame.pack(padx=5, pady=5)

path_entry = Entry(download_frame, width = 70)
path_entry.pack(padx=5, pady=5, side="left")

path_button = Button(download_frame, text="찾아보기", command=download_path)
path_button.pack(padx=5, pady=5, side="right")

# 옵션 설정
option_frame = LabelFrame(root, text="옵션 선택")
option_frame.pack(side="left")

# (크기 설정)
option_size = Label(option_frame, text="크기")
option_size.pack(side="left", padx=5)
size_values = ["150(원본)"]
size_combobox = ttk.Combobox(option_frame, height=1, values=size_values, state="readonly")
size_combobox.pack(side="left", padx=5)
size_combobox.current(0)

# (저장 유형 설정)
save_values = ["PNG", "JPG(Error)"]
save_combobox = ttk.Combobox(option_frame, height=2, values=save_values, state="readonly")
save_combobox.pack(side="right", padx=5)
save_combobox.current(0)
option_save = Label(option_frame, text="저장 유형")
option_save.pack(side="right", padx=5)

download_botton = Button(root, text="Download", bg="coral", command=download_button_click)
download_botton.pack(side="right", padx=10, pady=10)


root.resizable(False, False) # 창 크기 변경 불가
root.mainloop()

def frame():
    root = Tk()
    root.title("Instargram Profile Image Downloader")
    root.geometry()

    # URL 입력 (entry, button)
    url_frame = LabelFrame(root, text="Instargram URL")
    url_frame.pack()

    url_entry = Entry(url_frame, width=70)
    url_entry.pack(padx=5, pady=5, side="left")


    url_check_button = Button(url_frame, text="ENTER", command=enter_btn_cmd)
    url_check_button.pack(padx=5, pady=5, side="right")

    # Profile Image 확인할 수 있는 이미지 레이블 (label)
    profile_img_frame = LabelFrame(root, text="Image")
    profile_img_frame.pack(pady=20)

    profile_img_label = PhotoImage(file="./instagram.png") # 사진 파일을 가장 바깥 폴더에 넣어야 찾을 수 있다고 나온다.
    profile_label = Label(profile_img_frame, image=profile_img_label)
    profile_label.pack(padx=10, pady=10)

    # 저장 경로 설정 (entry, button)
    download_frame = LabelFrame(root, text="저장 경로")
    download_frame.pack(padx=5, pady=5)

    path_entry = Entry(download_frame, width = 70)
    path_entry.pack(padx=5, pady=5, side="left")

    path_button = Button(download_frame, text="찾아보기")
    path_button.pack(padx=5, pady=5, side="right")

    # 옵션 설정
    option_frame = LabelFrame(root, text="옵션 선택")
    option_frame.pack(side="left")

    # (크기 설정)
    option_size = Label(option_frame, text="크기")
    option_size.pack(side="left", padx=5)
    size_values = ["150(원본)", "300", "450", "600"]
    size_combobox = ttk.Combobox(option_frame, height=0, values=size_values, state="readonly")
    size_combobox.pack(side="left", padx=5)
    size_combobox.current(0)

    # (저장 유형 설정)
    save_values = ["PNG", "JPG"]
    save_combobox = ttk.Combobox(option_frame, height=2, values=save_values, state="readonly")
    save_combobox.pack(side="right", padx=5)
    save_combobox.current(0)
    option_save = Label(option_frame, text="저장 유형")
    option_save.pack(side="right", padx=5)

    download_botton = Button(root, text="Download", bg="coral")
    download_botton.pack(side="right", padx=10, pady=10)


    root.resizable(False, False) # 창 크기 변경 불가
    root.mainloop()





