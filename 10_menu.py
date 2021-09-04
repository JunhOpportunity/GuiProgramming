from tkinter import *

root = Tk()
root.title("progressbar")
root.geometry("640x480")

def create_new_file():
    print("새로운 파일을 생성합니다")

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0) # menu_file을 menu변수 안에 넣음
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 구분하는 선 만들기
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) # 창 종료
menu.add_cascade(label="File", menu=menu_file) # 가장 큰 메뉴, 이 안에 위에것들 있음

# Edit 메뉴
menu.add_cascade(label="Edit")

# Language 메뉴 (radio 버튼을 통해 택 1)
menu_lang = Menu(menu, tearoff=0)
menu.add_cascade(label="Language", menu=menu_lang)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="JAVA")
menu_lang.add_radiobutton(label="C++")

# View 메뉴 (check box 이용)
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=menu_view)
menu_view.add_checkbutton(label="Show MiniMap")


root.config(menu=menu)
root.mainloop()