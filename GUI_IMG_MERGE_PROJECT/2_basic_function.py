import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("new")

# 파일 추가 함수
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir="C:/") # 최초의 C:/ 경로를 보여줌

    # 사용자가 선택한 파일 목록을 리스트 프레임에 출력하도록 하기
    for file in files:
        list_file.insert(END, file)

# 파일 제거 함수
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로(folder)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':   # 사용자가 취소 누른 경우
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)


# 시작
def start():
    # 각 옵션들 값 확인하기
    print("가로넓이 : ", comb_width.get())
    print("간격 : ", comb_space.get())
    print("포맷 : ", comb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return
    
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left", padx=5, pady=5)

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right", padx=5, pady=5)

# 리스트 프레임
# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True, padx=5, pady=5)
scrollbar.config(command=list_file.yview)
# list_frame = Frame(root)
# list_frame.pack()

# scrollbar = Scrollbar(list_frame)
# scrollbar.pack(side="right", fill="y")

# list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
# list_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
# scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # ipad는 내부 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack( padx=5, pady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
comb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
comb_width.current(0)
comb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
comb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
comb_space.current(0)
comb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포멧 옵션
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
comb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
comb_format.current(0)
comb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5)


p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)





root.resizable(False, False)
root.mainloop()
