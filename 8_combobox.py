import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("640x480")

# values에다가 콤보박스 안에 들어갈 것들을 정의해주어야함
values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) # height는 한 번에 표시되는 목록의 개수
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 읽기 전용 / 사용자가 따로 입력 불가능
readonly_combobox.current(0) # 0번째 인덱스 값을 기본 선택 값으로 설정
readonly_combobox.pack()


def btncmd():
    print(combobox.get())    # 선택된 값 출력
    print(readonly_combobox.get())
btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()