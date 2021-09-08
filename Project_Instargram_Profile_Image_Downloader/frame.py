import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Instargram Profile Image Downloader")
root.geometry()

# URL 입력 (entry, button)
url_frame = LabelFrame(root, text="Instargram URL")
url_frame.pack()

url_entry = Entry(url_frame, width=70)
url_entry.pack(padx=5, pady=5, side="left")
url_entry.insert(0, "URL을 입력해주세요")

url_check_button = Button(url_frame, text="ENTER")
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

download_botton = Button(root, text="Download", bg="orchid")
download_botton.pack(side="right", padx=10, pady=10)

root.resizable(False, False) # 창 크기 변경 불가
root.mainloop()