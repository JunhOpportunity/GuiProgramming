from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack(side="right")
root.title("Windows 메모장")
# root.geometry("1000x700")
root.geometry("640x480")
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu.add_cascade(label="파일(F)", menu=menu_file)
scrollbar = Scrollbar(root)
txt = Text(root, yscrollcommand=scrollbar.set)
# 오른쪽 끝에 스크롤 바 제작하기

scrollbar.pack(side="right", fill="y")
scrollbar.config(command=txt.yview)

# 텍스트 입력 칸 만들기

txt.pack(side="left", fill="both", expand=True) # 꽉 차게

# 메뉴 제작하기
def create_file():
    # 파일 생성하기
    with open('file.txt', 'w' ,encoding="utf8") as file:
        file.write(txt.get("1.0", END))
def open_file():
    # 파일 열기
    with open('file.txt', 'r', encoding="utf8") as file:
        txt.insert(END, file.read())

menu_file.add_command(label = "열기", command=open_file)
menu_file.add_command(label = "저장", command=create_file)
menu_file.add_separator()
menu_file.add_command(label = "끝내기", command=exit)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")



root.config(menu=menu)
root.mainloop()